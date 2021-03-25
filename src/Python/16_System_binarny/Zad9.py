"""
Uzywajac operacji bitowych:
a) Zamien wielkie litery na male.
b) Zamien male litery na wielkie.
c) Zamien male litery na wielkie i wielkie na male.
"""


def wielkieNaMale(slowo):
    wynik = ""

    for litera in slowo:
        wynik += chr(ord(litera) | ord(" "))

    return wynik


def maleNaWielkie(slowo):
    wynik = ""

    for litera in slowo:
        wynik += chr(ord(litera) & ord("_"))

    return wynik


def odwrocWielkoscLiter(slowo):

    wynik = ""

    for litera in slowo:
        if litera >= "a" and litera <= "z":
            wynik += chr(ord(litera) ^ ord(" "))

        elif litera >= "A" and litera <= "Z":
            wynik += chr(ord(litera) ^ ord(" "))

        else:
            wynik += litera

    return wynik


if __name__ == "__main__":

    slowo = "KURCZAKU"
    wynik = "kurczaku"

    assert wielkieNaMale(slowo) == wynik

    slowo = "piesek"
    wynik = "PIESEK"

    assert maleNaWielkie(slowo) == wynik

    slowo = "wszedl Kotek na PloteK i mrUga"

    print(odwrocWielkoscLiter(slowo))
