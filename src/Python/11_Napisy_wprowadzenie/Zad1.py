"""
Odwroc napis.
"""

# Wersja 1
def odwroc_napis_v1(napis):
    return napis[::-1]


# Wersja 2
def odwroc_napis_v2(napis):
    if len(napis) <= 1:
        return napis

    return odwroc_napis_v2(napis[1:]) + napis[0]


# Wersja 3
def odwroc_napis_v3(napis):
    return "".join(reversed(napis))


# Testy Poprawnosci
napis = "abc"
wynik = "cba"

assert odwroc_napis_v1(napis) == wynik
assert odwroc_napis_v2(napis) == wynik
assert odwroc_napis_v3(napis) == wynik
