import xml.etree.ElementTree as ET
import argparse

def parseGroundTruth(inputFile, outputFile):
    partisanDistribution = {
        "right": {
            "false": 0,
            "true": 0
        },
        "left": {
            "false": 0,
            "true": 0
        },
        "least": {
            "false": 0,
            "true": 0
        },
        "right-center": {
            "false": 0,
            "true": 0
        },
        "left-center": {
            "false": 0,
            "true": 0
        },
        "all": {
            "false": 0,
            "true": 0
        }
    }

    articlesCount = 0

    stats_file = open(outputFile, 'w+')

    tree = ET.parse(inputFile)
    root = tree.getroot()
    for article in root:
        articlesCount += 1
        isHyperpartisan = article.attrib['hyperpartisan'];
        articleBias = article.attrib['bias'];
        partisanDistribution[articleBias][isHyperpartisan] += 1
        partisanDistribution["all"][isHyperpartisan] += 1
    print('parsed ', articlesCount, 'articles')

    print('Out of', articlesCount, 'articles:', file=stats_file)
    print(partisanDistribution["all"]['false'],'are not hyperpartisan', file=stats_file)
    print(partisanDistribution["all"]['true'],'are hyperpartisan\n', file=stats_file)

    for bias, distribution in partisanDistribution.items():
        if bias == 'all':
            continue
        print('Out of',distribution['false']+distribution['true'], bias, 'leaning articles:', file=stats_file)
        print(distribution['false'], 'are not hyperpartisan', file=stats_file)
        print(distribution['true'], 'are hyperpartisan\n', file=stats_file)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('inputFile', help="path to the ground truth training file")
    parser.add_argument('outputFile', help="path to the output file containing the distribution")
    args = parser.parse_args()
    parseGroundTruth(args.inputFile,args.outputFile)