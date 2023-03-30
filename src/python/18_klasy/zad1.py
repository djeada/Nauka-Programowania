"""
Tytul: Zaprojektuj klase Kolo.
Opis zadania: Napisz klase Kolo, ktora bedzie reprezentowala kolo. Klasa powinna zawierac nastepujace funkcje:
1. Konstruktor, ktory przyjmuje jedna liczbe jako argument, reprezentujaca promien kola. Domyslna wartoscia promienia powinno byc 1.
2. Funkcje obwod, ktora zwraca obwod kola.
3. Funkcje pole, ktora zwraca pole kola.
4. Funkcje, ktora wypisuje informacje o kole na standardowe wyjscie.
Napisz program, ktory przetestuje twoja klase. Stworz kolo o promieniu 3 i uzyj funkcji wypisujacej informacje o kole.

"""

import math

class Kolo:
    def __init__(self, promien=1):
        self.promien = promien

    def obwod(self):
        return 2 * math.pi * self.promien

    def pole(self):
        return math.pi * self.promien * self.promien

    def __str__(self):
        return f"Kolo o promieniu {self.promien:.2f}\nObwod: {self.obwod():.2f}\nPole: {self.pole():.2f}"

if __name__ == "__main__":
    kolo = Kolo(3)
    print(kolo)

