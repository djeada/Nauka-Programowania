import string

"""
Otrzymujesz napis reprezentujący zdanie. Zwróć listę składającą się ze 
słów zdania. Znaki interpunkcyjne nie są liczone jako słowa. 
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def test_podziel_zdanie_na_slowa():
    assert podziel_zdanie_na_slowa("Ala ma kota.") == ["Ala", "ma", "kota"]


if __name__ == "__main__":

    test_podziel_zdanie_na_slowa()
