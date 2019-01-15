from imports import *
from func import *

def extract(path,output_path):
    tree = ET.parse(path)
    root = tree.getroot()
    articleId = root.attrib['id']
    articleContent = "".join(root.itertext())
    file = open(output_path,"w") 
    file.write(articleContent)

extract(sys.argv[1], sys.argv[2])