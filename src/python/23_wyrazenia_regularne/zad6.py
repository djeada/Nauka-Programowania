"""
Tytul: Cyfry w slowach.
Tresc: Dostajesz napis reprezentujacy zdanie. Zapisz w liscie cyfry, ktore sa czescia slow. Cyfry oddzielone od liter spacja powinny zostac pominiete.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego", powinna zostac zwrocona lista: ["29", "37", "3891", "3"].

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
    oczekiwane = [
        "Folgujmy paniom nie sobie, ma rada",
        "Milujmy wiernie nie jest w nich przysada",
    ]

    assert wiersze_konczace_sie_napisem(tekst, napis) == oczekiwane


if __name__ == "__main__":
    test_wiersze_konczace_sie_napisem()

