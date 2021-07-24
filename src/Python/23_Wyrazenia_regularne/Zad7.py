"""
Znajdz wiersze zaczynajace sie od napisu A lub konczace sie napisem B. 
Wiersz moze byc zakonczony dowolnym znakiem interpunktcyjnym.
"""

import re

# Wersja 1
def zaczyna_sie_lub_konczy_v1(tekst, napis_a, napis_b):
    return [
        e
        for e in tekst.splitlines()
        if re.search(r"^{0}".format(napis_a), e, flags=re.M)
        or re.search(r"{0}[!?.,;]$".format(napis_b), e, flags=re.M)
    ]


if __name__ == "__main__":

    # Testy Poprawnosci
    tekst = """Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragną nie pragna tu zlota."""

    napis_a = "Mi"
    napis_b = "da"

    wynik = [
        "Folgujmy paniom nie sobie, ma rada;",
        "Milujmy wiernie nie jest w nich przysada.",
        "Milosci pragną nie pragna tu zlota.",
    ]

    assert zaczyna_sie_lub_konczy_v1(tekst, napis_a, napis_b) == wynik
