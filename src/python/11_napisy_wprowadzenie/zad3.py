"""
Tytul: Usun spacje ze zdania.
Tresc: Otrzymasz napis reprezentujacy zdanie. Usun spacje ze zdania.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "Alamakota".

"""
import string


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def liczba_slow_w_zdaniu(zdanie):
    return len(podziel_zdanie_na_slowa(zdanie))


def test_liczba_slow_w_zdaniu():
    assert liczba_slow_w_zdaniu("Ala ma kota.") == 3
    assert liczba_slow_w_zdaniu("Ala ma kota, a kot ma Ale.") == 7


if __name__ == "__main__":
    test_liczba_slow_w_zdaniu()

