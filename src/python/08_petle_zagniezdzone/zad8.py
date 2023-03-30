"""
Tytul: Trojkat Pascala.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat Pascala o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
1
11
121

"""
from math import pow


def trojkat_pascala(wysokosc):

    for i in range(wysokosc):
        for j in range(i + 1):
            print(pow(2, i) - pow(2, i - j) + pow(2, j), end=" ")
    print()


if __name__ == "__main__":

    print("Podaj wysokosc trojkata Pascala: ")
    wysokosc = int(input())
    trojkat_pascala(wysokosc)

