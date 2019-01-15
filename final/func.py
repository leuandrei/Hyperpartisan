from imports import json, re

def load_json(json_file_path):
	with open(json_file_path, "r") as fp2:
		text = fp2.read()
		source_dict = json.loads(text)
	fp2.close()
	return source_dict

def tokenize(text, patterns):
	tokens = []
	words = re.findall(patterns, text)
	for word in words:
		word = list(filter(None, word))
		if len(word) >= 1:
			tokens.append(word[0].lower())
	return tokens
