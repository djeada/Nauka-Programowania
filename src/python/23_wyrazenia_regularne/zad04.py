"""
Tytul: Sprawdz czy slowo wystepuje w zdaniu.
Tresc: Dostajesz dwa napisy. Sprawdz, czy drugi napis wystepuje w pierwszym jako pojedyncze slowo.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisow: “Siala baba mak.” oraz “babcia”, powinna zostac zwrocona wartosc logiczna: Falsz.

"""

import re


def czy_pierwszy_napis_zawiera_drugi_napis_v1(napis1, napis2):
    return napis2 in napis1


def czy_pierwszy_napis_zawiera_drugi_napis_v2(napis1, napis2):
    return re.search(napis2, napis1)


def test_czy_pierwszy_napis_zawiera_drugi_napis_v1():
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "kotek")
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "ma")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "Ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v1("Ala ma kota", "Ala ma")


def test_czy_pierwszy_napis_zawiera_drugi_napis_v2():
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "kotek")
    assert not czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "ma")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "Ala")
    assert czy_pierwszy_napis_zawiera_drugi_napis_v2("Ala ma kota", "Ala ma")


if __name__ == "__main__":
    test_czy_pierwszy_napis_zawiera_drugi_napis_v1()
    test_czy_pierwszy_napis_zawiera_drugi_napis_v2()
