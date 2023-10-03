"""
Tytul: Usun powtorzenia stojacych obok siebie znakow.
Tresc: Otrzymujesz napis. Twoim zadaniem jest usuniecie powtorzen stojacych obok siebie znakow i zachowanie tylko pierwszego wystapienia kazdego znaku.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrocony napis powinien brzmiec: “ABA”.

"""

# Wersja 1
def usun_powtarzajacych_sie_sasiadow_v1(napis):
    nowy_napis = ""
    ostatni_usuniety_znak = ""

    for i in range(len(napis) - 1):
        if not napis[i] == napis[i + 1]:
            nowy_napis += napis[i]
            ostatni_usuniety_znak = napis[i]

    if len(napis) and napis[-1] != ostatni_usuniety_znak:
        nowy_napis += napis[-1]

    return nowy_napis


# Testy Poprawnosci
def test_1():
    napis = "AAAAAAAAAABBBBBBBBA"
    wynik = "ABA"
    assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik


def test_2():
    napis = "XXXYYASFBY"
    wynik = "XYASFBY"
    assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik


def test_3():
    napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC"
    wynik = "C"
    assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik


def test_4():
    napis = ""
    wynik = ""
    assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik


def test_5():
    napis = "AAABB"
    wynik = "AB"
    assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik


def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


if __name__ == "__main__":
    main()
