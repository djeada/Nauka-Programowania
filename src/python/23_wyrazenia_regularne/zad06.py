"""
ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Otrzymujesz dwa napisy:

1. tekst wielowierszowy,
2. słowo lub fragment.

Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć się znakiem interpunkcyjnym).

### Wejście

Dwie części:

1. Tekst (wiele wierszy)
2. W osobnej linii: `koncowka`

*(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*

### Wyjście

Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.

### Przykład

**Wejście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

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
