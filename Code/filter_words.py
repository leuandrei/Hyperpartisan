from nltk import word_tokenize
from nltk.corpus import stopwords

text="Placeholder text"

def filtering(text):
    stopWords=set(stopwords.words('english'))
    words = word_tokenize(text)

    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    return wordsFiltered
print(filtering(text))
