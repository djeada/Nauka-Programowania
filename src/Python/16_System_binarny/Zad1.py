"""
Zamien liczbe binarna na jej odpowiednik w systemie dziesietnym
"""

# Wersja 1
def naDziesietnyV1(liczba):
    wynik = 0
    for i, v in enumerate(liczba[::-1]):
        wynik += (2 ** int(i)) * int(v)

    return wynik


# Testy poprawnosci
liczba = "0011"
wynik = 3
assert naDziesietnyV1(liczba) == wynik

liczba = "1111100"
wynik = 124
assert naDziesietnyV1(liczba) == wynik
