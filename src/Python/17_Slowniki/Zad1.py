"""
Wypisz słownik gdzie kluczami są liczby, a wartościami ich kwadraty.
"""

# Wersja 1
def zbudujSlownikV1(lista):

    slownik = {}

    for x in lista:
        slownik[x] = x ** 2

    return slownik


# Wersja 2
def zbudujSlownikV2(lista):
    return {x: x ** 2 for x in lista}


# Testy poprawnosci
lista = [3, 9, 2, -7, 1]
wynik = {3: 9, 9: 81, 2: 4, -7: 49, 1: 1}

assert zbudujSlownikV1(lista) == wynik
assert zbudujSlownikV2(lista) == wynik
