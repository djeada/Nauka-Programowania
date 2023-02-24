"""
Otrzymujesz napis reprezentujacy zdanie. Podziel zdanie na slowa. 
Posortuj slowa alfabetycznie i zapisz je w liscie. Pamietaj, znaki 
interpunkcyjne nie sa liczone jako slowa.
"""

import string


def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja zwraca liste slow ze zdania.
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def sortuj_slowa_w_zdaniu(zdanie):
    """
    Funkcja zwraca posortowana liste slow ze zdania.
    """
    return sorted(podziel_zdanie_na_slowa(zdanie))


def test_sortuj_slowa_w_zdaniu():
    assert sortuj_slowa_w_zdaniu("Lemur wygina smialo cialo") == ["Lemur", "cialo", "smialo", "wygina"]


if __name__ == "__main__":
    test_sortuj_slowa_w_zdaniu()
