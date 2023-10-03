"""
Tytul: Zamien znaki na kody ASCII.
Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z otrzymanych numerow, oddzielonych przecinkami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Robot", powinien zostac zwrocony napis: "82, 111, 98, 111, 116".

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
