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

def metoda1(path, articles_dict):
    tree = ET.parse(path)
    root = tree.getroot()
    articleId = root.attrib['id']
    articleContent = "".join(root.itertext())

    articleBias = articles_dict[articleId][1]
    articleIsHyperPartisan = articles_dict[articleId][0]

    if(articleIsHyperPartisan == 'false'):
        value = "NOT hyperpartisan"
    else:
        value = "hyperpartisan"

    article_hyperpartisan_prob = 0
    article_not_hyperpartisan_prob = 0
    article_token_count = 0

    articleTokens = tokenize(articleContent, patterns)
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
                # print (str(token_total_freq_in_dict) + ' ' + token)
                article_hyperpartisan_prob += (token_hyperpartisan_prob / token_total_freq_in_dict)
                article_not_hyperpartisan_prob += (token_not_hyperpartisan_prob / token_total_freq_in_dict)

    article_hyperpartisan_prob = float(article_hyperpartisan_prob) / float(article_token_count)
    article_not_hyperpartisan_prob = float(article_not_hyperpartisan_prob) / float(article_token_count)

    guess = "hyperpartisan" if article_hyperpartisan_prob > article_not_hyperpartisan_prob else "NOT hyperpartisan"

    print('article {articleId} classified as \'{classification}\' using method 1 with prob {prob}, expected \'{bias}\'. Guess: {is_correct}.'.format(articleId=articleId, classification = guess,prob=str(article_hyperpartisan_prob)[0:5] if article_hyperpartisan_prob > article_not_hyperpartisan_prob else str(article_not_hyperpartisan_prob)[0:5], bias = value, is_correct = "true" if guess == value else "false"))

articles_dict = load_json('../Code/articles-data.json')
metoda1(sys.argv[1], articles_dict)
