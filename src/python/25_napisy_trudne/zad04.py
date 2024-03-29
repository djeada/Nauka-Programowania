"""
Tytul: Usun powtorzenia znakow.
Tresc: Otrzymujesz napis. Twoim zadaniem jest usuniecie powtorzen kazdego znaku w napisie. Kazdy znak moze wystapic tylko raz.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrocony napis powinien brzmiec: “AB”.

"""

# Wersja 1
def usun_powtorzenia_v1(napis):
    nowy_napis = ""
    for znak in napis:
        if znak not in nowy_napis:
            nowy_napis += znak

    return nowy_napis


# Testy Poprawnosci
def test_1():
    napis = "AAAAAAAAAABBBBBBBBA"
    wynik = "AB"
    assert usun_powtorzenia_v1(napis) == wynik


def test_2():
    napis = "XXXYYASFBY"
    wynik = "XYASFB"
    assert usun_powtorzenia_v1(napis) == wynik


def test_3():
    napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC"
    wynik = "C"
    assert usun_powtorzenia_v1(napis) == wynik


def test_4():
    napis = ""
    wynik = ""
    assert usun_powtorzenia_v1(napis) == wynik


def test_5():
    napis = "AAABBAABBABABABA"
    wynik = "AB"
    assert usun_powtorzenia_v1(napis) == wynik


def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


if __name__ == "__main__":
    main()
