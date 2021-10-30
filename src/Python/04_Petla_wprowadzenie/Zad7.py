"""
Dla pobranej liczby, wyświetl liczbę Pi podniesioną do 
potęgi równej pobranej liczbie. Wynik powinien być 
zaokrąglony do dwóch miejsc po przecinku.
"""

from math import pi

if __name__ == "__main__":

    print("Podaj liczbę: ")
    liczba = int(input())

    wynik = 1
    for i in range(liczba):
        wynik = wynik * pi

    print("Wynik: ", round(wynik, 2))