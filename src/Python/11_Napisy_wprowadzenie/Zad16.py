"""
Miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji na ktorych napisy maja rozne znaki.
"""

# Wersja 1
def odlegloscHammingaV1(napisA, napisB):
    if len(napisA) != len(napisB):
        return -1

    wynik = 0

    for i in range(len(napisA)):
        if napisA[i] != napisB[i]:
            wynik += 1

    return wynik


# Wersja 2
def odlegloscHammingaV2(napisA, napisB):
    if len(napisA) != len(napisB):
        return -1
    return sum(znakA != znakB for znakA, znakB in zip(napisA, napisB))


# Testy Poprawnosci
assert odlegloscHammingaV1("adam", "axam") == 1
assert odlegloscHammingaV2("adam", "axam") == 1

assert odlegloscHammingaV1("xxbab", "bbabb") == 4
assert odlegloscHammingaV2("xxbab", "bbabb") == 4

assert odlegloscHammingaV1("ror", "rorr") == -1
assert odlegloscHammingaV2("ror", "rorr") == -1
