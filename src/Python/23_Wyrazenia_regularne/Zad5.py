"""
Z ciagu znakow wypisz cyfry.
"""

import re

# Wersja 1
def tylkoCyfryV1(slowo):
    return re.sub("[^\d]", "", slowo)


# Testy Poprawnosci
slowo = "numer 32.19 wyzej niz 31.17"
wynik = "32193117"

assert tylkoCyfryV1(slowo) == wynik
