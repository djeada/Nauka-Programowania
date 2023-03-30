"""
Tytul: Zamien wszystkie male litery na duze.
Tresc: Otrzymasz napis. Zmien wszystkie male litery na duze.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Rumcajs", powinien zostac zwrocony napis: "RUMCAJS".

"""


def usun_spacje(zdanie):
    return zdanie.replace(" ", "")


def test_usun_spacje():
    assert usun_spacje("Ala ma kota") == "Alamakota"


if __name__ == "__main__":

    test_usun_spacje()

