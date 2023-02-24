"""
Otrzymujesz napis. Przy uzyciu operatorow bitowych:
a) Zamien wielkie litery na male litery.
b) Zamien male litery na wielkie litery.
c) Zamien male litery na wielkie litery i wielkie litery na male litery.
"""


def wielkie_na_male(slowo):
    """
    Funkcja zamienia wielkie litery na male litery.
    """
    wynik = ""

    for litera in slowo:
        wynik += chr(ord(litera) | ord(" "))

    return wynik


def male_na_wielkie(slowo):
    """
    Funkcja zamienia male litery na wielkie litery.
    """
    wynik = ""

    for litera in slowo:
        wynik += chr(ord(litera) & ord("_"))

    return wynik


def odwroc_wielkosc_liter(slowo):
    """
    Funkcja zamienia male litery na wielkie litery i wielkie litery na male litery.
    """
    wynik = ""

    for litera in slowo:
        if litera >= "a" and litera <= "z":
            wynik += chr(ord(litera) ^ ord(" "))

        elif litera >= "A" and litera <= "Z":
            wynik += chr(ord(litera) ^ ord(" "))

        else:
            wynik += litera

    return wynik


def test_wielkie_na_male():
    assert wielkie_na_male("KURCZAKU") == "kurczaku"


def test_male_na_wielkie():
    assert male_na_wielkie("piesek") == "PIESEK"


def test_odwroc_wielkosc_liter():
    assert (
        odwroc_wielkosc_liter("wszedl Kotek na PloteK i mrUga")
        == "WSZEDL kOTEK NA pLOTEk I MRuGA"
    )


if __name__ == "__main__":

    test_wielkie_na_male()
    test_male_na_wielkie()
    test_odwroc_wielkosc_liter()
