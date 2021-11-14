'''
Napisz klase Zespolona reprezentujaca liczbe zespolona. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy dwie liczby jako argumenty. Pierwsza liczba reprezentuje czesc 
rzeczywista, a druga czesc urojona liczby zespolonej. Domyslne wartosci dla obu argumentow to 0.
b) Funkcje zwracajace wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie, 
dzielenie). Jesli jest to mozliwe nalezy przeciazyc operatory: +, -, *, /.
c) Funkcja wypisujaca informacje o liczbie zespolonej na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Zespolona. Jesli jest to mozliwe nalezy 
przeciazyc operatory ==, !=.
e) Funkcja modul, zwracajaca modul liczby zespolonej. 

Napisz program testujacy twoja klase. Stworz liczby zespolone: A(9, 12) i B(-3, -3). Wypisz na 
standardowe wyjscie informacje o utworzonych liczbach zespolonych oraz ich sume, roznice pierwszej 
i drugiej, iloraz pierwszej przez druga oraz iloczyn liczb zespolonych.
'''

import math

class Zespolona:
    def __init__(self, rzeczywista=0, urojona=0):
        self.rzeczywista = rzeczywista
        self.urojona = urojona

    def __add__(self, other):
        return Zespolona(self.rzeczywista + other.rzeczywista, self.urojona + other.urojona)

    def __sub__(self, other):
        return Zespolona(self.rzeczywista - other.rzeczywista, self.urojona - other.urojona)

    def __mul__(self, other):
        return Zespolona(self.rzeczywista * other.rzeczywista - self.urojona * other.urojona,
                         self.rzeczywista * other.urojona + self.urojona * other.rzeczywista)

    def __truediv__(self, other):
        return Zespolona((self.rzeczywista * other.rzeczywista + self.urojona * other.urojona) / (other.rzeczywista ** 2 + other.urojona ** 2),
                         (self.urojona * other.rzeczywista - self.rzeczywista * other.urojona) / (other.rzeczywista ** 2 + other.urojona ** 2))

    def __str__(self):
        return f'{self.rzeczywista:.2f} + {self.urojona:.2f}i'

    def __eq__(self, other):
        return self.rzeczywista == other.rzeczywista and self.urojona == other.urojona

    def __ne__(self, other):
        return self.rzeczywista != other.rzeczywista or self.urojona != other.urojona

    def modul(self):
        return math.sqrt(self.rzeczywista ** 2 + self.urojona ** 2)


if __name__ == "__main__":
    
    zespolona_a = Zespolona(9, 12)
    zespolona_b = Zespolona(-3, -3)

    print(f'Liczba zespolona A: {zespolona_a}')
    print(f'Liczba zespolona B: {zespolona_b}')
    print(f'Suma liczb zespolonych A i B: {zespolona_a + zespolona_b}')
    print(f'Roznica liczb zespolonych A i B: {zespolona_a - zespolona_b}')
    print(f'Iloczyn liczb zespolonych A i B: {zespolona_a * zespolona_b}')
    print(f'Iloraz liczb zespolonych A i B: {zespolona_a / zespolona_b}')
    print(f'Modul liczby zespolonej A: {zespolona_a.modul()}')
    print(f'A == B: {zespolona_a == zespolona_b}')
    print(f'A != B: {zespolona_a != zespolona_b}')