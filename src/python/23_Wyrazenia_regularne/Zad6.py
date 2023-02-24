"""
Otrzymujesz dwa napisy. Znajdz wiersze w pierwszym napisie 
konczace sie drugim napisem. Wiersz moze byc zakonczony 
dowolnym znakiem interpunkcyjnym.
"""

import re


def wiersze_konczace_sie_napisem(tekst, koniec):
    """
    Zwraca wszystkie wiersze konczace sie napisem koniec.
    """
    wiersze = re.split("\n|\.|\?|\!|\;|\:", tekst)
    return [wiersz for wiersz in wiersze if wiersz.endswith(koniec)]


def test_wiersze_konczace_sie_napisem():
    tekst = """Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota."""
    napis = "da"
    oczekiwane=["Folgujmy paniom nie sobie, ma rada", "Milujmy wiernie nie jest w nich przysada"]

    assert wiersze_konczace_sie_napisem(tekst, napis) == oczekiwane

if __name__ == "__main__":
    test_wiersze_konczace_sie_napisem()
