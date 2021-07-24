"""
Oblicz silnie z podanej liczby.	
"""

# Wersja 1
def silnia_v1(liczba):
    wynik = 1

    for i in range(liczba):
        wynik *= i + 1

    return wynik


# Wersja 2
def silnia_v2(liczba):
    if liczba <= 0:
        return 1

    return liczba * silnia_v2(liczba - 1)


# Testy Poprawnosci
liczba = 3
wynik = 6

assert silnia_v1(liczba) == wynik
assert silnia_v2(liczba) == wynik
