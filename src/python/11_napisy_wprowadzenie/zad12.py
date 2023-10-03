"""
Tytul: Usun spacje ze zdania.
Tresc: Otrzymasz napis reprezentujacy zdanie. Usun spacje ze zdania.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "Alamakota".

"""


def usun_spacje(zdanie):
    return zdanie.replace(" ", "")


def test_usun_spacje():
    assert usun_spacje("Ala ma kota") == "Alamakota"


if __name__ == "__main__":

    test_usun_spacje()
