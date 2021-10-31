"""
Dla pobranej liczby, wyswietl liczbe Pi podniesiona do 
potegi rownej pobranej liczbie. Wynik powinien byc 
zaokraglony do dwoch miejsc po przecinku.
"""

from math import pi

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    wynik = 1
    for i in range(liczba):
        wynik = wynik * pi

    print("Wynik: ", round(wynik, 2))
