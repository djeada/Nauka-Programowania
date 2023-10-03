"""
Tytul: Odwroc napis.
Tresc: Zmien otrzymany napis, tak aby zapisany byl on od tylu.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "barszcz", powinien zostac zwrocony napis: "zczsrab".

"""


def odwroc_v1(napis):
    return napis[::-1]


def odwroc_v2(napis):
    nowy_napis = ""
    i = len(napis) - 1
    while i >= 0:
        nowy_napis += napis[i]
        i -= 1
    return nowy_napis


def test_odwroc_v1():
    assert odwroc_v1("ala ma kota") == "kota ma ala"
    assert odwroc_v1("") == ""
    assert odwroc_v1("ala") == "ala"
    assert odwroc_v1("kot") == "tko"


def test_odwroc_v2():
    assert odwroc_v2("ala ma kota") == "kota ma ala"
    assert odwroc_v2("") == ""
    assert odwroc_v2("ala") == "ala"
    assert odwroc_v2("kot") == "tko"


if __name__ == "__main__":

    test_odwroc_v1()
    test_odwroc_v2()
