"""
Oblicz silnie z podanej liczby.	
"""

# Wersja 1
def silniaV1(liczba):
    wynik = 1

    for i in range(liczba):
        wynik *= i + 1

    return wynik


# Wersja 2
def silniaV2(liczba):
    if liczba <= 0:
        return 1

    return liczba * silniaV2(liczba - 1)


# Testy Poprawnosci
liczba = 3
wynik = 6

assert silniaV1(liczba) == wynik
assert silniaV2(liczba) == wynik
