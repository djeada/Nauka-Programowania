"""
Tytul: Znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.
Tresc: Otrzymasz napis. Znajdz znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista znakow.
Przyklad:
Dla otrzymanego napisu: "Slon", powinna zostac zwrocona lista: ['o', 'n'].

"""


def na_male(napis):
    return napis.lower()


def test_na_male():
    assert na_male("test") == "test"
    assert na_male("Test") == "test"
    assert na_male("TEST") == "test"


if __name__ == "__main__":
    test_na_male()

