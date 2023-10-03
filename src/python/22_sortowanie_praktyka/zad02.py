"""
Tytul: Sortowanie slow w zdaniu.
Tresc: Masz dany napis reprezentujacy zdanie. Podziel to zdanie na slowa, posortuj je alfabetycznie i zapisz w liscie. Znaki interpunkcyjne nie sa liczone jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisu "Lemur wygina smialo cialo" powinno zostac zwrocone ["Lemur", "cialo", "smialo", "wygina"].

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
    assert sortuj_slowa_w_zdaniu("Lemur wygina smialo cialo") == [
        "Lemur",
        "cialo",
        "smialo",
        "wygina",
    ]


if __name__ == "__main__":
    test_sortuj_slowa_w_zdaniu()
