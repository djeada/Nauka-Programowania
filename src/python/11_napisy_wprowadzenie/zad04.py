"""
Tytul: Zamien wszystkie male litery na duze.
Tresc: Otrzymasz napis. Zmien wszystkie male litery na duze.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Rumcajs", powinien zostac zwrocony napis: "RUMCAJS".

"""


def na_male(napis):
    return napis.lower()


def test_na_male():
    assert na_male("test") == "test"
    assert na_male("Test") == "test"
    assert na_male("TEST") == "test"


if __name__ == "__main__":
    test_na_male()
