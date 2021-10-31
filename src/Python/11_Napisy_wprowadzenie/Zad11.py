import string

"""
Otrzymujesz napis reprezentujący zdanie. 
Oblicz średnią długość słów w zdaniu. 
Znaki interpunkcyjne nie są liczone jako słowa. 
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def srednia_dlugosc_slow(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    wynik = sum(len(slowo) for slowo in slowa) / len(slowa)
    return int(wynik)


def test_srednia_dlugosc_slow():
    assert srednia_dlugosc_slow("Kaczka lubi wiosne.") == 5
    assert srednia_dlugosc_slow("Ile to   ma :  slow w swoim zdaniu na   koniec?") == 3


if __name__ == "__main__":
    test_srednia_dlugosc_slow()
