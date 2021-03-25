"""
Odwroc napis.
"""

# Wersja 1
def odwrocNapisV1(napis):
    return napis[::-1]


# Wersja 2
def odwrocNapisV2(napis):
    if len(napis) <= 1:
        return napis

    return odwrocNapisV2(napis[1:]) + napis[0]


# Wersja 3
def odwrocNapisV3(napis):
    return "".join(reversed(napis))


# Testy Poprawnosci
napis = "abc"
wynik = "cba"

assert odwrocNapisV1(napis) == wynik
assert odwrocNapisV2(napis) == wynik
assert odwrocNapisV3(napis) == wynik
