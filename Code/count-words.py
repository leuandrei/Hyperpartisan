import json
import xml.etree.ElementTree as ET
import sys
import pprint
import re
import nltk

nltk.download('punkt')

REGEX_FLAGS = re.VERBOSE | re.MULTILINE | re.IGNORECASE

re_email = '(([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6}))'
re_url = '((http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?)'
re_ipv4 = '([0-9]{1,3}([.][0-9]{1,3}){3})'
re_phone = '(((\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})|( (0\d{3}) ((\ -\ \d{6}) | ([-/]\d{2}(-\d{2}){2})) ) )'
re_hyphen_words = "([-']?[a-zA-Z]+([-'][a-zA-Z]+)*[-']?)"
re_words = "([a-zA-Z]+)"

regexes = [
    #re_ipv4,
    #re_email,
    #re_url,
    #re_phone,
    re_hyphen_words,
    re_words]

patterns = re.compile('|'.join(x for x in regexes), REGEX_FLAGS)

stop_words_file = open("../data/stopwords.txt", "r+")
stop_words = [word[:-1] for word in stop_words_file]



def nltk_tokenize(text):
	return nltk.word_tokenize(text)

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

max_article_parse = 800000
article_count = 0

for event, article in ET.iterparse(articles):
	if article_count == max_article_parse:
		break
	if article.tag == "article":
		if article_count % 10000 == 0:
			print('Parsing article {article_count}'.format(article_count = article_count))
		article_count += 1
		articleId = article.attrib['id']
		articleContent = "".join(article.itertext())
		articleBias = articles_dict[articleId][1]
		articleIsHyperPartisan = articles_dict[articleId][0]

		articleTokens = tokenize(articleContent)
		for token in articleTokens:
			if token not in stop_words:
				if token in word_dict[articleIsHyperPartisan]:
					word_dict[articleIsHyperPartisan][token] += 1
				else:
					word_dict[articleIsHyperPartisan][token] = 1
		article.clear()

outputJSON = open('../data/word-count.json', 'w+')

final_word_dict = {
	"true": {},
	"false": {}
}

for key in sorted(word_dict['true'], key=word_dict['true'].get, reverse=True):
	if word_dict['true'][key] > 10:
		final_word_dict['true'][key] = word_dict['true'][key]
	
for key in sorted(word_dict['false'], key=word_dict['false'].get, reverse=True):
	if word_dict['false'][key] > 10:
		final_word_dict['false'][key] = word_dict['false'][key]	

print(json.dumps(final_word_dict, indent=4), file=outputJSON)
