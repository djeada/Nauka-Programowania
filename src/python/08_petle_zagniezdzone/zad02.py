"""
Tytul: Trojkat prostokatny rownoboczny
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat prostokatny rownoboczny o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
*
**
***

"""


def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(i + 1):
            print("*", end="")
        print()


if __name__ == "__main__":

    wysokosc = int(input("Podaj wysokosc trojkata: "))
    trojkat(wysokosc)
