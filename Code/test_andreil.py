import unittest
from andreil import Andreil

a = Andreil()

class TestAndreiFunctions(unittest.TestCase):
    def test_tokenizer(self):
        test_text = "This text. shall be, replaced:"
        list = a.tokenize(test_text)
        for i in list:
            self.assertTrue(" " not in str(i))

    def test_frequency(self):
        test_text = "A dict within a dict within another dict"
        dict = a.compute_frequency(test_text)
        for i in dict:
            self.assertFalse(int(dict.get(str(i)))<0)

    def test_parser(self):
        test_text = "<tag> orice numar este <=5"
        list = a.parser(test_text)
        self.assertFalse('<' in str(list))