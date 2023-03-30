"""
Tytul: Odwrocony trojkat prostokatny rownoboczny
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze, zaczynajac od podstawy, trojkat prostokatny rownoboczny o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 4 powinno zostac wypisane:
****
***
**
*

"""


def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc - i):
            print("*", end=" ")
        print()


if __name__ == "__main__":

    print("Podaj wysokosc trojkata: ")
    wysokosc = int(input())

    trojkat(wysokosc)

