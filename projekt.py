import random
from tkinter import *

class MyError(Exception):
    pass

class UnknownError(MyError):
    pass

class IncorrectData(MyError):
    pass

class RegulyGry():
    def __init__(self):
        self._n1 = random.randint(1, 6)
        self._n2 = random.randint(1, 6)
        self._n3 = random.randint(1, 6)
        self._n4 = random.randint(1, 6)
        self.num = [self._n1, self._n2, self._n3, self._n4]
        self.attempts_left = 12
    
    def peek(self):
        """Podejrzyj wygenerowane rozwiązanie"""
        ret = str(self.num)
        ret = "Rozwiązaniem było: " + ret
        return ret
    
    def changeSol(self):
        """Ustaw rozwiązanie na wybrane, przydatne przy testowaniu"""
        self._n1 = 1
        self._n2 = 2
        self._n3 = 3
        self._n4 = 4
        
    def nextAttempt(self):
        """Pobierz kolejną odpowiedź od użytkownika, prześlij ją do oceny"""
        print("Pozostało prób:", self.attempts_left)
        inp = input("Podaj cztery cyfry (bez odstępów): ")
        correct = 0
        if inp == "RESET":
            self.reset()
        elif (len(inp) != 4) or ([True for x in inp if x not in "123456"]):    
            print("Niepoprawny format.")
        else:
            self.attempts_left -= 1
            correct = self.evaluateAnswer(inp)
        return correct
        
    def evaluateAnswer(self, guess):
        """Porównaj podaną odpowiedź, zwróc trafienia pełne i częściowe"""
        hits = 0
        places = 0
        g1, g2, g3, g4 = [int(x) for x in guess]
        g_num = [g1, g2, g3, g4]
        #num_freq - tablica przechowujaca informacje o ilosci kazdej z cyfr 1-6 w nietrafionym kodzie
        #g_freq - tablica przechowujaca informacje o ilosci kazdej z cyfr 1-6 w nietrafionej odpowiedzi uzytkownika
        num_freq = [0,0,0,0,0,0]
        g_freq = [0,0,0,0,0,0]
        for x in range(len(g_num)):
            if g_num[x] == self.num[x]:
                hits += 1
            else:
                cur_num = self.num[x]
                num_freq[cur_num - 1] += 1
                cur_num = g_num[x]
                g_freq[cur_num - 1] += 1
        for x in range(len(num_freq)):
            while num_freq[x] > 0:
                if g_freq[x] > 0:
                    places += 1
                    g_freq[x] -= 1
                num_freq[x] -= 1
        return hits, places
    
    def reset(self):
        """Wylosuj kolejny kod, przywróc 12 prób użytkownikowi"""
        self._n1 = random.randint(1, 6)
        self._n2 = random.randint(1, 6)
        self._n3 = random.randint(1, 6)
        self._n4 = random.randint(1, 6)
        self.num = [self._n1, self._n2, self._n3, self._n4]
        self.attempts_left = 12
    
    def victoryPopUp(self):
        """Zgłoś wygraną przez użytkownika"""
        return "Wygrana"
    
    def lossPopUp(self):
        """Zgłoś przegraną przez użytkownika"""
        return "Przegrana"
        
    def mainLoop(self):
        """Pętla zajmująca się działaniem programu"""
        while self.attempts_left > 0:
            correct = self.nextAttempt()
            if correct == 4:
                print(self.victoryPopUp())
                break
        if correct != 4:
            print(self.lossPopUp())
        
    def sendInput(self, inp):
        """Sprawdź i prześlij do oceny odp. użytkownika, analogicznie do nextAttempt() ale przyjmująca odpowiedź jako arg."""
        correct = 0
        if (len(inp) != 4) or ([True for x in inp if x not in "123456"]):    
            return "Niepoprawny format.", 0, 0
        else:
            self.attempts_left -= 1
            correct, places = self.evaluateAnswer(inp)
        return self.checkCond(correct, places)
    
    def checkCond(self, correct, places):
        """Metoda sprawdzająca warunki końcowe programu, analogiczna do jednokrotnego wywołania pętli z funkcji mainLoop"""
        if correct == 4:
            return self.victoryPopUp(), 4, 0
        elif self.attempts_left < 1 and correct != 4:
            return self.lossPopUp(), -1, -1
        else:
            atts = str(self.attempts_left)
            atts = "Pozostało prób: " + atts
            correct = str(correct)
            correct = "Pełne trafienia: " + correct
            places = str(places)
            places = "Poprawne liczby na złych miejscach: " + places
            return atts, correct, places
        
    def oszust(self):
        """Wyświetl komunikat oraz poprawny kod"""
        ann = str(self.num)
        ann = "Tere fere. Rozwiązaniem było: " + ann
        return ann, 0
        
class OszukaneReguly(RegulyGry):
    def peek(self):
        """Pokaż informację o oszustwie"""
        return "Oszukiwałem!"
    
    def oszust(self):
        """Powiadow użytkownika o wygranej"""
        ann = "Złapałeś/łaś mnie!"
        return ann, 1
    
    def evaluateAnswer(self, guess):
        """Porównaj podaną odpowiedź, zwróc niepoprawne trafienia pełne i częściowe"""
        true_hits = 0
        true_places = 0
        g1, g2, g3, g4 = [int(x) for x in guess]
        g_num = [g1, g2, g3, g4]
        #find the correct answers
        num_freq = [0,0,0,0,0,0]
        g_freq = [0,0,0,0,0,0]
        for x in range(len(g_num)):
            if g_num[x] == self.num[x]:
                true_hits += 1
            else:
                cur_num = self.num[x]
                num_freq[cur_num - 1] += 1
                cur_num = g_num[x]
                g_freq[cur_num - 1] += 1
        for x in range(len(num_freq)):
            while num_freq[x] > 0:
                if g_freq[x] > 0:
                    true_places += 1
                    g_freq[x] -= 1
                num_freq[x] -= 1
        #make the answers incorrect
        if true_hits == 1 or true_hits == 2:
            hits = true_hits + random.choice([-1, 1])
        elif true_hits == 3 or true_hits == 4:
            hits = true_hits - 1
        else:
            hits = true_hits + 1
            
        if true_places == 1 or true_places == 2:
            places = true_places + random.choice([-1, 1])
        elif true_places == 3 or true_places == 4:
            places = true_places - 1    
        else:
            places = true_places + 1
        return hits, places

if __name__ == '__main__':
    cheat = random.choice([0, 1])
    if cheat == 0:
        reguly = RegulyGry()
    else:
        reguly = OszukaneReguly()

    def reset():
        reguly.reset()
    
    def peek():
        reguly.attempts_left = 0
        label.config(text = (reguly.peek()))
    
    def getInput():
        user_input = text_box.get("1.0","end-1c")
        atts, correct, places = reguly.sendInput(user_input)
        label.config(text = atts)
        hints_1.config(text = correct)
        hints_2.config(text = places)

    def oszust():
        ann, mode = reguly.oszust()
        label.config(text = ann)
        
    
    root = Tk()
    root.title('App')
    root.geometry("600x400")
    label = Label(root, text="Mastermind", font=30, fg="blue")
    label.pack()
    reset_button = Button(root, text="RESET", width=8, command=reset)
    reset_button.pack()
    text_box = Text(root, height=1, width=12)
    text_box.pack()
    label = Label(root, text = "Pozostało prób: 12")
    label.pack()
    send_button = Button(root, text="Confirm guess", width=14, command = lambda:getInput())
    send_button.pack()
    peek_button = Button(root, text="Give up and reveal the code", width=20, command=peek)
    peek_button.pack()
    hints_1 = Label(root, text="Pełne trafienia: 0")
    hints_1.pack()
    hints_2 = Label(root, text="Poprawne liczby na złych miejscach: 0")
    hints_2.pack()
    oszust_button = Button(root, text="Oszust!", width=8, command=oszust)
    oszust_button.pack()
    root.mainloop()
