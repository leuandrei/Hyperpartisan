from filter_words import filtering
from nltk.corpus import stopwords

def test_filter(text):
    count=0
    stopWords=set(stopwords.words('english'))
    list=filtering(text)
    for i in list:
        #self.assertFalse(str(i) in stopwords)
        if (str(i) not in stopWords):
            count=count+1
    print(float(count/len(list)))

def test_stress(n, text):
    for i in range(1000000):
        filtering(text)
        print("done filtering:"+str(i))

test_filter("This is some placeholder text")
test_stress(10, "Placeholder text that has a number of words, numerals, wrdos wrettin worng and other beautiful test cases worth trying to break down or at least slow the program enough for it to become unusable")