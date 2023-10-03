"""
Tytul: Litera X.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere X o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 4 powinno zostac wypisane:
*   *
* *
* *
*   *

"""


def litera_x(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc):
            if j == i or j == wysokosc - i - 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":

    print("Podaj wysokosc litery X: ")
    wysokosc = int(input())

    litera_x(wysokosc)
