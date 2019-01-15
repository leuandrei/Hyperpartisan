from imports import *
from func import *

stop_words_file = open("../data/stopwords.txt", "r+")
stop_words = [word[:-1] for word in stop_words_file]

re_hyphen_words = "([-']?[a-zA-Z]+([-'][a-zA-Z]+)*[-']?)"
re_words = "([a-zA-Z]+)"

words_freq_dict = load_json('../data/word-count.json')

regexes = [re_hyphen_words,re_words]
REGEX_FLAGS = re.VERBOSE | re.MULTILINE | re.IGNORECASE
patterns = re.compile('|'.join(x for x in regexes), REGEX_FLAGS)
articles_dict = load_json('../Code/articles-data.json')

article = sys.argv[1]

print('Article {articleId} classified as {classification} using both methods with prob {prob}. Guess: {is_correct}'.format(articleId = getArticleId(article), classification = getClassification(article), is_correct = getCorrectness(article))
