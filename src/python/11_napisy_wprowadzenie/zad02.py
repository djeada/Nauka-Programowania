"""
Tytul: Policz wystapienia znaku.
Tresc: Dla podanego napisu i znaku, znajdz liczbe wystapien tego znaku w napisie.
Dane wejsciowe: Napis oraz znak.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "klamra" oraz znaku 'a', powinno zostac zwrocone: 2.

"""


def liczba_wystapien(napis, znak):
    return napis.count(znak)


def test_liczba_wystapien():
    assert liczba_wystapien("ala ma kota", "a") == 3
    assert liczba_wystapien("ala ma kota", "k") == 1


if __name__ == "__main__":

    test_liczba_wystapien()
