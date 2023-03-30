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

def odwroc(napis):
    return napis[::-1]

def odwroc_slowa(zdanie):

    wynik = " ".join([odwroc(slowo) for slowo in podziel_zdanie_na_slowa(zdanie)])

    for i, znak in enumerate(zdanie):
        if znak in string.punctuation:
            wynik = wynik[:i] + znak + wynik[i:]

    return wynik

def test_odwroc_slowa():
    assert odwroc_slowa("Ala ma kota.") == "alA am atok."

if __name__ == "__main__":

    test_odwroc_slowa()

