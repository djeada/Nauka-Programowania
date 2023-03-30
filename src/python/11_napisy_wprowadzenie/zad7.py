"""
Tytul: Odleglosc Hamminga.
Tresc: Otrzymujesz dwa napisy o rownej dlugosci. Oblicz odleglosc Hamminga miedzy dwoma otrzymanymi napisami. Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji, na ktorych napisy maja rozne znaki.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych napisow: “adam” i “axam”, powinna zostac zwrocona liczba: 1.

"""


def znaki_na_ascii(napis):

    nowy_napis = ""
    for znak in napis:
        nowy_napis += str(ord(znak)) + ", "

    return nowy_napis[:-2]


def test_znaki_na_ascii():
    assert znaki_na_ascii("abcdef") == "97, 98, 99, 100, 101, 102"
    assert (
        znaki_na_ascii("ala ma kota")
        == "97, 108, 97, 32, 109, 97, 32, 107, 111, 116, 97"
    )


if __name__ == "__main__":

    test_znaki_na_ascii()

