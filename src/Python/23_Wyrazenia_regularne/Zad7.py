"""
Znajdz wiersze zaczynajace sie od napisu A lub konczace sie napisem B. 
Wiersz moze byc zakonczony dowolnym znakiem interpunktcyjnym.
"""

import re

# Wersja 1
def zaczynaSieLubKonczyV1(tekst, napisA, napisB):
    return [
        e
        for e in tekst.splitlines()
        if re.search(r"^{0}".format(napisA), e, flags=re.M)
        or re.search(r"{0}[!?.,;]$".format(napisB), e, flags=re.M)
    ]


if __name__ == "__main__":

    # Testy Poprawnosci
    tekst = """Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragną nie pragna tu zlota."""

    napisA = "Mi"
    napisB = "da"

    wynik = [
        "Folgujmy paniom nie sobie, ma rada;",
        "Milujmy wiernie nie jest w nich przysada.",
        "Milosci pragną nie pragna tu zlota.",
    ]

    assert zaczynaSieLubKonczyV1(tekst, napisA, napisB) == wynik
