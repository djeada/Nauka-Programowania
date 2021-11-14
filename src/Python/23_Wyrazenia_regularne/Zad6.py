"""
Otrzymujesz dwa napisy. Znajdz wiersze w pierwszym napisie 
konczace sie drugim napisem. Wiersz moze byc zakonczony 
dowolnym znakiem interpunkcyjnym.
"""

import re


def zaczyna_sie_lub_konczy(tekst, napis_a, napis_b):
    """
    Funkcja zwraca True jesli tekst zaczyna sie lub konczy napis_a
    lub napis_b.
    """
    return [
        wiersz
        for wiersz in tekst.splitlines()
        if re.search(r"^{0}".format(napis_a), wiersz, flags=re.M)
           or re.search(r"{0}[!?.,;]$".format(napis_b), wiersz, flags=re.M)
    ]


def test_zaczyna_sie_lub_konczy():
    tekst = """Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota."""

    napis_a = "Mi"
    napis_b = "da"

    oczekiwane = [
        "Folgujmy paniom nie sobie, ma rada;",
        "Milujmy wiernie nie jest w nich przysada.",
        "Milosci pragna nie pragna tu zlota.",
    ]

    assert zaczyna_sie_lub_konczy(tekst, napis_a, napis_b) == oczekiwane


if __name__ == "__main__":
    test_zaczyna_sie_lub_konczy()
