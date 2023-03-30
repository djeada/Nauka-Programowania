"""
Tytul: Sortowanie znakow w napisie.
Tresc: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu "Ala ma kota" powinno zostac zwrocone " Aaaaklmot".

"""


def sortuj_napis(napis):
    return "".join(sorted(napis))


def test_sortuj_napis():
    assert sortuj_napis("Ala ma kota") == "  Aaaaklmot"
    assert sortuj_napis("kot ma Ale") == "  Aaeklmot"


if __name__ == "__main__":
    test_sortuj_napis()

