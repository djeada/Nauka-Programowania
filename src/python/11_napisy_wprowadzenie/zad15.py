"""
Tytul: Slowa ze zdania jako osobne elementy listy.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zwroc liste slow zdania. Znaki interpunkcyjne nie sa liczone jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: “Ala ma kota”, powinna zostac zwrocona lista: [“Ala”, “ma”, “kota”].

"""
import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def test_podziel_zdanie_na_slowa():
    assert podziel_zdanie_na_slowa("Ala ma kota.") == ["Ala", "ma", "kota"]


if __name__ == "__main__":

    test_podziel_zdanie_na_slowa()
