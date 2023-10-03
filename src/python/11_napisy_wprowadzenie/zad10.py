"""
Tytul: Znajdz najdluzsze/najkrotsze slowo w zdaniu.
Tresc: Otrzymasz napis reprezentujacy zdanie. Znajdz:
a) najdluzsze slowo w zdaniu,
b) najkrotsze slowo w zdaniu.
Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, zwroc to slowo sposrod nich, ktore wystepuje w zdaniu jako pierwsze. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe:
a) Napis.
b) Napis.
Przyklad:
a) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "Kaczka".
b) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "lubi".

"""
import string


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
