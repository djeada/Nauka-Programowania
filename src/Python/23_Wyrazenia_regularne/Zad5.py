"""
Z ciagu znakow wypisz cyfry.
"""

import re

# Wersja 1
def tylko_cyfry_v1(slowo):
    return re.sub("[^\d]", "", slowo)


# Testy Poprawnosci
slowo = "numer 32.19 wyzej niz 31.17"
wynik = "32193117"

assert tylko_cyfry_v1(slowo) == wynik
