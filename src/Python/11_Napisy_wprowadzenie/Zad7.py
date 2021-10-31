"""
Otrzymujesz napis. Zamien wszystkie znaki napisu na odpowiadajace 
im numery w tablicy ASCII. Podmien otrzymany napis na napis 
skladajacy sie z otrzymanych numerow oddzielonych przecinkami.
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
