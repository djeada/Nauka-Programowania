'''
Napisz klase Kolo reprezentujaca kolo. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy jedna liczbe jako argument, reprezentujaca promien kola. Domyslna wartosc promienia to 1.
b) Funkcja obwod, zwracajaca obwod kola.
c) Funkcja pole, zwracajaca pole kola.
d) Funkcja wypisujaca informacje o kole na standardowe wyjscie.

Napisz program testujacy twoja klase. Stworz kolo o promieniu rownym 3 i uzyj funkcji wypisujacej informacje o kole.
'''

import math

class Kolo:

    def __init__(self, promien=1):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien
    
    def pole(self):
        return math.pi * self.promien * self.promien
    
    def __str__(self):
        return f'Kolo o promieniu {self.promien:.2f}\nObwod: {self.obwod():.2f}\nPole: {self.pole():.2f}'
    

if __name__ == "__main__":
    kolo = Kolo(3)
    print(kolo)