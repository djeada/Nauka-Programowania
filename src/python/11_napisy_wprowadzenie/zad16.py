"""
Tytul: Odleglosc Hamminga.
Tresc: Otrzymujesz dwa napisy o rownej dlugosci. Oblicz odleglosc Hamminga miedzy dwoma otrzymanymi napisami. Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji, na ktorych napisy maja rozne znaki.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych napisow: “adam” i “axam”, powinna zostac zwrocona liczba: 1.

"""


def odleglosc_hamminga(napis_a, napis_b):
    if len(napis_a) != len(napis_b):
        return -1

    licznik = 0
    for i in range(len(napis_a)):
        if napis_a[i] != napis_b[i]:
            licznik += 1
    return licznik


def test_odleglosc_hamminga():

    assert odleglosc_hamminga("abc", "abc") == 0
    assert odleglosc_hamminga("abc", "abd") == 1
    assert odleglosc_hamminga("abc", "abcd") == -1
    assert odleglosc_hamminga("xxx", "abc") == 3


if __name__ == "__main__":

    test_odleglosc_hamminga()
