'''
Napisz klase Punkt reprezentujaca punkt w ukladzie kartezjanskim. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy dwie liczby jako argumenty. Pierwsza liczba reprezentuje wspolrzedna x, a druga 
wspolrzedna y. Domyslne wartosci dla obu argumentow wynosza 0.
b) Funkcja statyczna odleglosc, zwracajaca odleglosc miedzy dwoma punktami (obiektami klasy Punkt).
c) Funkcja wypisujaca informacje o punkcie na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Punkt. Jesli jest to mozliwe nalezy przeciazyc 
operatory ==, !=.

Napisz program testujacy twoja klase. Stworz punkty: A(5, 5) oraz B(-3, -3). Wypisz na standardowe wyjscie 
informacje o utworzonych punktach oraz odleglosc miedzy nimi.
'''

import math

class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def odleglosc(p1, p2):
        return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

    def __str__(self):
        return f'Punkt({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    

if __name__ == "__main__":
    punkt_a = Punkt(5, 5)
    punkt_b = Punkt(-3, -3)
    print(f'Odleglosc miedzy punktami A {punkt_a} i B {punkt_b} wynosi: {Punkt.odleglosc(punkt_a, punkt_b):.2f}.')