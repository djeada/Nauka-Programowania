"""
Podziel zdanie na czesci wzgledem znakow interpunkcyjnych.
Jesli wynikiem podzialu jest pusty napis, pomin.
"""

import re

# Wersja 1
def podziel_zdanie_v1(zdanie):
    return [x for x in re.split(r"[,.!?]", zdanie) if x]


# Testy Poprawnosci
zdanie = "hej, pan slimak! tak to ja. chodzcie juz zaspiewam wam."
wynik = ["hej", " pan slimak", " tak to ja", " chodzcie juz zaspiewam wam"]

assert podziel_zdanie_v1(zdanie) == wynik
