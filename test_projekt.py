import unittest
from projekt import *

class Test(unittest.TestCase):
    
    
    def test_(self):
        reguly = RegulyGry()
        reguly.changeSol()
        hits, places = reguly.evaluateAnswer(self, 1411)
        self.assertEqual(hits, 1)
        self.assertEqual(places, 1)

        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
        

if __name__ == '__main__':
    unittest.main()