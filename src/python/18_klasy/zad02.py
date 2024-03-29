"""
Tytul: Zaprojektuj klase Punkt.
Tresc: Napisz klase Punkt, ktora bedzie reprezentowala punkt w ukladzie kartezjanskim. Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje dwa argumenty (liczby). Pierwsza liczba reprezentuje wspolrzedna x, a druga wspolrzedna y. Domyslne wartosci dla obu argumentow powinny wynosic 0.
2. Funkcje statyczna odleglosc, ktora zwraca odleglosc miedzy dwoma punktami (obiektami klasy Punkt).
3. Funkcje, ktora wypisuje informacje o punkcie na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Punkt. Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.
Napisz program, ktory przetestuje twoja klase. Stworz punkty: A (5, 5) oraz B (-3, -3). Wypisz na standardowe wyjscie informacje o utworzonych punktach oraz odleglosc miedzy nimi.

"""

import math


class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def odleglosc(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def __str__(self):
        return f"Punkt({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


if __name__ == "__main__":
    punkt_a = Punkt(5, 5)
    punkt_b = Punkt(-3, -3)
    print(
        f"Odleglosc miedzy punktami A {punkt_a} i B {punkt_b} wynosi: {Punkt.odleglosc(punkt_a, punkt_b):.2f}."
    )
