import abc
import nltk.tokenize

class TextReceiver:
    receivedText=""
    @abc.abstractmethod
    def getText(self, text):
        pass

class ResultSender:
    resultText=""
    @abc.abstractmethod
    def sendText(self, text):
        pass

class Tokenizer:
    inputText=TextReceiver()
    tokenizedText=ResultSender()
    def tokenize(self, text):
        pass

class FrequencyComputer:
    wordList=list()
    frequencyList=list()
    dictionary=TextReceiver()
    frequencies=ResultSender()

# Singleton/SingletonPattern.py

class Singleton:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not Singleton.instance:
            Singleton.instance = Singleton.__OnlyOne(arg)
        else:
            Singleton.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)

x = Singleton('sausage')
print(x)
a = Singleton('sausage')
print(a)
y = Singleton('eggs')
print(y)
z = Singleton('spam')
print(z)
print(x)
print(y)
print(x)
print(y)
print(z)
"""output = '''
<__main__.__OnlyOne instance at 0076B7AC>sausage
<__main__.__OnlyOne instance at 0076B7AC>eggs
<__main__.__OnlyOne instance at 0076B7AC>spam
<__main__.__OnlyOne instance at 0076B7AC>spam
<__main__.__OnlyOne instance at 0076B7AC>spam
<__main__.OnlyOne 1instance at 0076C54C>
<__main__.OnlyOne instance at 0076DAAC>
<__main__.OnlyOne instance at 0076AA3C>
'''"""



class Facade:
    """
    Know which subsystem classes are responsible for a request.
    Delegate client requests to appropriate subsystem objects.
    """

    def __init__(self):
        self._subsystem_1 = Subsystem1()
        self._subsystem_2 = Subsystem2()

    def operation(self):
        self._subsystem_1.operation1()
        self._subsystem_1.operation2()
        self._subsystem_2.operation1()
        self._subsystem_2.operation2()


class Subsystem1:
    """
    Implement subsystem functionality.
    Handle work assigned by the Facade object.
    Have no knowledge of the facade; that is, they keep no references to
    it.
    """

    def operation1(self):
        pass

    def operation2(self):
        pass


class Subsystem2:
    """
    Implement subsystem functionality.
    Handle work assigned by the Facade object.
    Have no knowledge of the facade; that is, they keep no references to
    it.
    """

    def operation1(self):
        pass

    def operation2(self):
        pass


def main():
    facade = Facade()
    facade.operation()


if __name__ == "__main__":
    main()

print(nltk.word_tokenize("<xml><article>Acesta aets un artciel</article></xml>"))

from aspect_l import logger

class Andreil:
    @logger
    def tokenize(self, text):
        return nltk.word_tokenize(text)

    @logger
    def compute_frequency(self, text):
        dictionary=dict()
        list = nltk.word_tokenize(text)
        for i in list:
            if (str(i) not in dictionary):
                dictionary[str(i)]="1"
            else:
                dictionary[str(i)]=str(int(dictionary.get(str(i)))+1)
        return dictionary

    @logger
    def parser(self, text):
        list = nltk.word_tokenize(text)
        ok=0
        i=0
        while i<len(list):
            if (str(list[i]) == '>' and ok == 1):
                list.remove(list[i])
                ok = 0
            elif (str(list[i])=='<'):
                ok=1
                list.remove(list[i])
            elif (ok==1):
                list.remove(list[i])
            else:
                i=i+1
        return list
print("APELURILE DE JOS:")

a = Andreil()
test_text = "This text. shall be, replaced:"
print(a.tokenize(test_text))

test_text = "A dict within a dict within another dict"
print(a.compute_frequency(test_text))

test_text = "<tag> orice numar este <=5"
print(a.parser(test_text))
