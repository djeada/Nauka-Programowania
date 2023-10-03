"""
Tytul: Wyodrebnij cyfry z tekstu.
Tresc: Dostajesz napis. Zwroc napis skladajacy sie z cyfr wystepujacych w tym napisie.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu: “Terminator2001”, powinien zostac zwrocony napis: “2001”.

"""

import re


def odfiltruj_cyfry(slowo):
    return re.sub("[^\d]", "", slowo)


def test_odfiltruj_cyfry():
    assert odfiltruj_cyfry("numer 32.19 wyzej niz 31.17") == "32193117"


if __name__ == "__main__":
    test_odfiltruj_cyfry()
