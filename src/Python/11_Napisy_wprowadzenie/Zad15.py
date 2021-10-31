import string

"""
Otrzymujesz napis reprezentujacy zdanie. Zwroc liste skladajaca sie ze 
slow zdania. Znaki interpunkcyjne nie sa liczone jako slowa. 
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def test_podziel_zdanie_na_slowa():
    assert podziel_zdanie_na_slowa("Ala ma kota.") == ["Ala", "ma", "kota"]


if __name__ == "__main__":

    test_podziel_zdanie_na_slowa()
