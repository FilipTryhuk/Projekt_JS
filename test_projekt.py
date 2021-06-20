import unittest
from projekt import *

class Test(unittest.TestCase):
    
    def test_incorrentGuess(self):
        reguly = LogikaGry()
        reguly.changeSol()
        hits, places = reguly.evaluateAnswer([5, 6, 5, 6])
        self.assertEqual(hits, 0)
        self.assertEqual(places, 0)

    def test_correctNumbersWrongPlaces(self):
        reguly = LogikaGry()
        reguly.changeSol()
        hits, places = reguly.evaluateAnswer([4, 3, 2, 1])
        self.assertEqual(hits, 0)
        self.assertEqual(places, 4)
        
    def test_twoCorrectTwoInWrongPlaces(self):
        reguly = LogikaGry()
        reguly.changeSol()
        hits, places = reguly.evaluateAnswer([1, 2, 4, 3])
        self.assertEqual(hits, 2)
        self.assertEqual(places, 2)        
        
    def test_showCorrectAnswerThenGuessCorrectly(self):
        reguly = LogikaGry()
        res =  reguly.peek()
        res = res.split(" ", 2)
        ans = [res[2][1], res[2][4], res[2][7], res[2][10]]
        hits, places = reguly.evaluateAnswer(ans)
        self.assertEqual(hits, 4)
        self.assertEqual(places, 0)
        
    def test_noAttempsLeft(self):
        reguly = LogikaGry()
        reguly.changeSol() 
        for i in range(12):
            ans, hits, places = reguly.sendInput(str(5555))
        self.assertEqual(ans, "Przegrana")
    
    def test_incorrectFormat(self):
        reguly = LogikaGry()
        reguly.sendInput(str(123456))
        self.assertEqual(reguly.attempts_left, 12)
        
    def test_oszustWhenRegulyCorrect(self):
        reguly = LogikaGry()
        ann, mode = reguly.oszust()
        self.assertEqual(ann[:10], "Tere fere.")
    
    def test_oszustWhenRegulyIncorrect(self):
        reguly = OszukaneReguly()
        ann, mode = reguly.oszust()
        self.assertEqual(ann[:18], "Złapałeś/łaś mnie!")
    
    def test_restGameContinuePlaying(self):
        reguly = LogikaGry()
        reguly.changeSol()
        for i in range(10):
            reguly.sendInput(str(5555))
        reguly.reset()
        reguly.changeSol()
        for i in range(5):
            reguly.sendInput(str(5555))
        self.assertEqual(reguly.attempts_left, 7)
        
if __name__ == '__main__':
    unittest.main()
