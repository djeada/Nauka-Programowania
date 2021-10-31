import string

"""
Otrzymujesz napis reprezentujacy zdanie. Znajdz: 
a) Najdluzsze slowo w zdaniu.
b) Najkrotsze slowo w zdaniu. 

Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, zwroc to 
slowo sposrod nich, ktore wystepuje w zdaniu jako pierwsze. 
Znaki interpunkcyjne nie sa liczone jako slowa.  
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def najdluzsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return max(slowa, key=len)


def najkrotsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return min(slowa, key=len)


def test_najdluzsze_slowo():
    assert najdluzsze_slowo("Ala ma kota.") == "kota"


def test_najkrotsze_slowo():
    assert najkrotsze_slowo("Ala ma kota.") == "ma"


if __name__ == "__main__":

    test_najdluzsze_slowo()
    test_najkrotsze_slowo()
