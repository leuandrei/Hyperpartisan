import json
import xml.etree.ElementTree as ET
import sys
import pprint
import re

REGEX_FLAGS = re.VERBOSE | re.MULTILINE | re.IGNORECASE

re_email = '(([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6}))'
re_url = '((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?)'
re_ipv4 = '([0-9]{1,3}([.][0-9]{1,3}){3})'
re_phone = '(((\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})|( (0\d{3}) ((\ -\ \d{6}) | ([-/]\d{2}(-\d{2}){2})) ) )'
re_hyphen_words = '([A-Z]\w+(-[A-Z]\w+)+)'
re_words = '(\w+)'

regexes = [
    re_ipv4,
    re_email,
    re_url,
    re_phone,
    re_hyphen_words,
    re_words]

patterns = re.compile('|'.join(x for x in regexes), REGEX_FLAGS)

def tokenize(text):
	tokens = []
	words = re.findall(patterns, text)
	for word in words:
		word = list(filter(None, word))
		if len(word) >= 1:
			tokens.append(word[0].lower())
	return tokens

def load_json(json_file_path):
	with open(json_file_path, "r") as fp2:
		text = fp2.read()
		source_dict = json.loads(text)
	fp2.close()
	return source_dict

articles_dict = load_json('articles-data.json')

word_dict = {
	"true": {},
	"false": {}
}

articles = '../data/articles-training-20180831.xml'

max_article_parse = 10000
article_count = 0

for event, article in ET.iterparse(articles):
	if article_count == max_article_parse:
		break
	if article.tag == "article":
		article_count += 1
		articleId = article.attrib['id']
		articleContent = "".join(article.itertext())
		articleBias = articles_dict[articleId][1]
		articleIsHyperPartisan = articles_dict[articleId][0]

		articleTokens = tokenize(articleContent)
		for token in articleTokens:
			if token in word_dict[articleIsHyperPartisan]:
				word_dict[articleIsHyperPartisan][token] += 1
			else:
				word_dict[articleIsHyperPartisan][token] = 1

final_true_dict = { k:v for k,v in word_dict['true'].items() if v>10}
final_false_dict = { k:v for k,v in word_dict['false'].items() if v>10}

final_true_dict = sorted(final_true_dict.items(), key=lambda kv: kv[1], reverse=True)
final_false_dict = sorted(final_false_dict.items(), key=lambda kv: kv[1], reverse=True)

final_dict = {'true':final_true_dict, 'false':final_false_dict}

pp = pprint.PrettyPrinter(indent=4)

outputFile = open('../data/word-count.txt', 'w+')

print('In', max_article_parse, 'articles the following words have been found:\n', file=outputFile)
pprint.pprint(final_dict, outputFile)

#sorted_word_dict = sorted(word_dict.items(), key=lambda kv: kv[1])
#print(sorted_word_dict)

#
#		hp = articles_dict[id][0]
#		bias = articles_dict[id][1]
