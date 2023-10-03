"""
Tytul: Liczba pi.
Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi tyle razy, ile wynosi ta liczba, z dokladnoscia do tylu miejsc po przecinku, ile wynosi otrzymana liczba.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 2, powinno zostac wypisane:
3,14
3,14

"""
from math import pi

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    print(f"Liczba Pi {liczba} razy: ")

    for i in range(liczba):
        print(f"{i+1}. {pi:.{liczba}f}")
