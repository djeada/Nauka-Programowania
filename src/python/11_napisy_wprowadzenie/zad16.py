"""
Tytul:Wypisz pionowo slowa, z ktorych sklada sie zdanie.
Tresc: Otrzymasz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe. Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Kilka napisow.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinno zostac wypisane: "Ala", "ma", "kota".

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

