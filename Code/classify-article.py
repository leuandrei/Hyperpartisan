import json
import xml.etree.ElementTree as ET
import sys
import pprint
import re
import nltk

nltk.download('punkt')

re_hyphen_words = "([-']?[a-zA-Z]+([-'][a-zA-Z]+)*[-']?)"
re_words = "([a-zA-Z]+)"

stop_words_file = open("../data/stopwords.txt", "r+")
stop_words = [word[:-1] for word in stop_words_file]

regexes = [
    #re_ipv4,
    #re_email,
    #re_url,
    #re_phone,
    re_hyphen_words,
    re_words]

REGEX_FLAGS = re.VERBOSE | re.MULTILINE | re.IGNORECASE
patterns = re.compile('|'.join(x for x in regexes), REGEX_FLAGS)

def load_json(json_file_path):
	with open(json_file_path, "r") as fp2:
		text = fp2.read()
		source_dict = json.loads(text)
	fp2.close()
	return source_dict

words_freq_dict = load_json('../data/word-count.json')
articles_dict = load_json('articles-data.json')

def tokenize(text):
	tokens = []
	words = re.findall(patterns, text)
	for word in words:
		word = list(filter(None, word))
		if len(word) >= 1:
			tokens.append(word[0].lower())
	return tokens



articles = '../data/articles-training-20180831.xml'

article_count = 0
max_article_parse = 100

for event, article in ET.iterparse(articles):
	if article_count == max_article_parse:
		break
	if article.tag == "article":
		article_count += 1
		articleId = article.attrib['id']
		articleContent = "".join(article.itertext())
		articleBias = articles_dict[articleId][1]
		articleIsHyperPartisan = articles_dict[articleId][0]
		
		article_hyperpartisan_prob = 0
		article_not_hyperpartisan_prob = 0
		article_token_count = 0

		articleTokens = tokenize(articleContent)
		for token in articleTokens:
			if token not in stop_words:
				article_token_count += 1

				token_hyperpartisan_prob = 0
				token_not_hyperpartisan_prob = 0

				token_total_freq_in_dict = 0

				if token in words_freq_dict['true']:
					token_total_freq_in_dict += words_freq_dict['true'][token]
					token_hyperpartisan_prob += words_freq_dict['true'][token]

				if token in words_freq_dict['false']:
					token_total_freq_in_dict += words_freq_dict['false'][token]
					token_not_hyperpartisan_prob += words_freq_dict['false'][token]

				if token_total_freq_in_dict > 0:
					article_hyperpartisan_prob += token_hyperpartisan_prob / token_total_freq_in_dict
					article_not_hyperpartisan_prob += token_not_hyperpartisan_prob / token_total_freq_in_dict
		article.clear()

		article_hyperpartisan_prob = article_hyperpartisan_prob / article_token_count
		article_not_hyperpartisan_prob = article_not_hyperpartisan_prob / article_token_count

		if article_hyperpartisan_prob > article_not_hyperpartisan_prob:
			print('article {articleId} classified as hyperpartisan with prob {prob}, expected {bias}'.format(articleId=articleId, prob=article_hyperpartisan_prob, bias=articleIsHyperPartisan))
		else:
			print('article {articleId} classified as not hyperpartisan with prob {prob}, expected {bias}'.format(articleId=articleId, prob=article_not_hyperpartisan_prob, bias=articleIsHyperPartisan))
