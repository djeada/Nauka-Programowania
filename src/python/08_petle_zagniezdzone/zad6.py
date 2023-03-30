"""
Tytul: Litera Z.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere Z o wysokosci rownej tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 5 powinno zostac wypisane:
*****
*
*
*
*****

"""


def litera_z(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc):
            if i == 0 or i == wysokosc - 1 or j == wysokosc - i - 1:
                print("Z", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":

    print("Podaj wysokosc litery Z: ")
    wysokosc = int(input())

    litera_z(wysokosc)

