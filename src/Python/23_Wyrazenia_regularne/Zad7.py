"""
Otrzymujesz napis. Podziel go wzgledem znakow interpunkcyjnych i 
zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu 
otrzymanych napisow.
"""

import re


def podziel_zdanie(zdanie):
    return [elem for elem in re.split(r"[,.!?]", zdanie) if elem]


def test_podziel_zdanie():
    zdanie = "hej, pan slimak! tak to ja. chodzcie to zaspiewam wam."
    oczekiwane = ["hej", " pan slimak", " tak to ja", " chodzcie to zaspiewam wam"]
    assert podziel_zdanie(zdanie) == oczekiwane


if __name__ == '__main__':
    test_podziel_zdanie()
