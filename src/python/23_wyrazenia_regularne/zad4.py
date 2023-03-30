"""
Tytul: Wiersze konczace sie okreslonym napisem.
Tresc: Dostajesz dwa napisy. Znajdz wiersze w pierwszym napisie konczace sie drugim napisem. Wiersz moze byc zakonczony dowolnym znakiem interpunkcyjnym.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisow:
> Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota.
oraz
> da
powinna zostac zwrocona lista: [“Folgujmy paniom nie sobie, ma rada;”, “Milujmy wiernie nie jest w nich przysada.”]

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

