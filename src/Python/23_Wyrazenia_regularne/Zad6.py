"""
Podziel zdanie na czesci wzgledem znakow interpunkcyjnych.
Jesli wynikiem podzialu jest pusty napis, pomin.
"""

import re

# Wersja 1
def podzielZdanieV1(zdanie):
    return [x for x in re.split(r"[,.!?]", zdanie) if x]


# Testy Poprawnosci
zdanie = "hej, pan slimak! tak to ja. chodzcie juz zaspiewam wam."
wynik = ["hej", " pan slimak", " tak to ja", " chodzcie juz zaspiewam wam"]

assert podzielZdanieV1(zdanie) == wynik
