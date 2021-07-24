"""
Miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji na ktorych napisy maja rozne znaki.
"""

# Wersja 1
def odleglosc_hamminga_v1(napis_a, napis_b):
    if len(napis_a) != len(napis_b):
        return -1

    wynik = 0

    for i in range(len(napis_a)):
        if napis_a[i] != napis_b[i]:
            wynik += 1

    return wynik


# Wersja 2
def odleglosc_hamminga_v2(napis_a, napis_b):
    if len(napis_a) != len(napis_b):
        return -1
    return sum(znakA != znakB for znakA, znakB in zip(napis_a, napis_b))


# Testy Poprawnosci
assert odleglosc_hamminga_v1("adam", "axam") == 1
assert odleglosc_hamminga_v2("adam", "axam") == 1

assert odleglosc_hamminga_v1("xxbab", "bbabb") == 4
assert odleglosc_hamminga_v2("xxbab", "bbabb") == 4

assert odleglosc_hamminga_v1("ror", "rorr") == -1
assert odleglosc_hamminga_v2("ror", "rorr") == -1
