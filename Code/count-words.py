from t import *
dict = load_json('articles-data.json')

articles = 'articles-training-20180831.xml'

article_start_pattern = re.compile('<article id="([0-9]{7})"')

with open(articles) as fp:
	lines = fp.readlines()

i = 0

for line in lines:
	id = re.match(article_start_pattern, line)

	#daca am facut match
	if id !=None:
		id = id.group(1)
		hp = dict[id][0]
		bias = dict[id][1]
		print id, hp, bias
		#stim id-ul articolului curent si hp si bias






	i+= 1
	if i > 100:
		break

'''
5 structuri de date:

left, right, lc, rc, neutral


'''
