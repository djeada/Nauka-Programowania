"""
Wypisz słownik gdzie kluczami są liczby, a wartościami ich kwadraty.
"""

# Wersja 1
def zbuduj_slownik_v1(lista):

    slownik = {}

    for x in lista:
        slownik[x] = x ** 2

    return slownik


# Wersja 2
def zbuduj_slownik_v2(lista):
    return {x: x ** 2 for x in lista}


# Testy poprawnosci
lista = [3, 9, 2, -7, 1]
wynik = {3: 9, 9: 81, 2: 4, -7: 49, 1: 1}

assert zbuduj_slownik_v1(lista) == wynik
assert zbuduj_slownik_v2(lista) == wynik
