"""
Tytul: Zaprojektuj klase Ksztalt oraz klasy potomne Kolo i Kwadrat.
Tresc: Zaprojektuj klase Ksztalt oraz klasy potomne Kolo i Kwadrat. Napisz program testujacy te klasy.

"""

import math

class Ksztalt:
    def __init__(self):
        raise NotImplementedError("Nie zaimplementowano konstruktora")

    def pole(self):
        raise NotImplementedError("Nie zaimplementowano funkcji pole")

    def obwod(self):
        raise NotImplementedError("Nie zaimplementowano funkcji obwod")

    def __str__(self):
        raise NotImplementedError("Nie zaimplementowano funkcji __str__")

class Kolo(Ksztalt):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return math.pi * self.promien ** 2

    def obwod(self):
        return 2 * math.pi * self.promien

    def __str__(self):
        return f"Kolo o promieniu {self.promien}"

class Kwadrat(Ksztalt):
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

    def obwod(self):
        return 4 * self.bok

    def __str__(self):
        return f"Kwadrat o boku {self.bok}"

if __name__ == "__main__":

    kolo = Kolo(5)
    print(f"{kolo}")
    print(f"Pole: {kolo.pole():.2f}")
    print(f"Obwod: {kolo.obwod():.2f}")
    print()

    kwadrat = Kwadrat(5)
    print(f"{kwadrat}")
    print(f"Pole: {kwadrat.pole():.2f}")
    print(f"Obwod: {kwadrat.obwod():.2f}")

