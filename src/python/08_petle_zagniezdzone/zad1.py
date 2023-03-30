"""
Tytul: Kwadrat
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze kwadrat o boku rownym tej liczbie.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 2 powinno zostac wypisane:
**
**

"""


def kwadrat(bok):
    for i in range(bok):
        for j in range(bok):
            print("*", end="")
        print()


if __name__ == "__main__":

    bok = int(input("Podaj bok kwadratu: "))
    kwadrat(bok)

