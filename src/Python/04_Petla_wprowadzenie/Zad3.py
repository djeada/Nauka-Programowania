"""
Dla pobranej liczby, wypisz liczbe Pi tyle razy 
ile wynosi pobrana liczba, z dokladnoscia do tylu 
miejsc po przecinku ile wynosi pobrana liczba.
"""
from math import pi

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    print(f"Liczba Pi {liczba} razy: ")

    for i in range(liczba):
        print(f"{i+1}. {pi:.{liczba}f}")
