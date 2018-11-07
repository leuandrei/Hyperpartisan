import re, json

def make_json(source_dict, json_file_path):
	#The additional dump parameters make it more readable for human eyes.
	with open(json_file_path, 'w') as fp:
	    json.dump(source_dict, fp, sort_keys=True, indent=4, separators=(',', ': '))
	fp.close()

def load_json(json_file_path):
	with open(json_file_path, "r") as fp2:
		text = fp2.read()
		source_dict = json.loads(text)
	fp2.close()
	return source_dict


articles = 'articles-training-20180831.xml'
tags = 'ground-truth-training-20180831.xml'

with open(tags) as fp:
	lines = fp.readlines()

fp.close()

i = 0

dict = {}
id_pattern = re.compile('id=\'([0-9]{7})\'')
hp_pattern = re.compile('hyperpartisan=\'(true|false)\'')
bias_pattern = re.compile('bias=\'(right|left|least|right-center|left-center)\'')

for line in lines:
	### extragem cele 3 informatii relevante
	id = re.search(id_pattern, line)
	hp = re.search(hp_pattern, line)
	bias = re.search(bias_pattern, line)

	if id != None:
		# print id.group(1)
		id = id.group(1)
	if hp != None:
		# print hp.group(1)
		hp = hp.group(1)
	if bias != None:
		# print bias.group(1)
		bias = bias.group(1)

	### le adaugam in dictionar
	if id!=None:
		dict[id] = [hp, bias]

	# i+= 1
	# if i > 20:
	# 	break

make_json(dict, 'articles-data.json')

# for el in dict:
# 	print el, dict[el]
