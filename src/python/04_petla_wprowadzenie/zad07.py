"""
Tytul: Potega liczby Pi.
Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi podniesiona do potegi rownej tej liczbie. Wynik powinien zostac zaokraglony do dwoch miejsc po przecinku.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad: Dla otrzymanej liczby 1, powinna zostac wypisana liczba 3,14.

"""

from math import pi

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    wynik = 1
    for i in range(liczba):
        wynik = wynik * pi

    print("Wynik: ", round(wynik, 2))
