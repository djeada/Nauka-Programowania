r"""
ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Wczytaj tekst wielowierszowy i końcówkę (np. `da`). Wypisz wszystkie wiersze tekstu, które **kończą się** podaną końcówką. Wiersz może mieć po końcówce znaki interpunkcyjne `.` `,` `;` `:` `!` `?` oraz spacje — w dowolnej liczbie — i nadal się liczy.

Końcówka nie musi być całym słowem: wiersz `Folgujmy paniom nie sobie, ma rada;` kończy się na `da`. Wielkość liter ma znaczenie. Wiersze wypisuj w niezmienionej postaci (razem z interpunkcją).

### Wejście

* 1. linia: `n` — liczba wierszy tekstu
* kolejne `n` linii: tekst
* ostatnia linia: końcówka (same litery)

### Wyjście

* Pasujące wiersze, każdy w osobnej linii, w kolejności występowania w tekście,
* `Brak wierszy.` — jeśli żaden wiersz nie pasuje.

### Ograniczenia

* $1 \le n \le 100$

### Przykład

**Wejście:**

```
4
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

### Uwagi

* Kotwica `$` oznacza koniec napisu, np. wzorzec `da[.,;:!? ]*$` pasuje do `rada;` i `przysada.`, ale nie do `dama`. Pamiętaj o `re.escape()` dla wczytanej końcówki.

"""

import re


def wiersze_konczace_sie(wiersze, koncowka):
    """Zwraca wiersze kończące się końcówką (po niej może być interpunkcja i spacje)."""
    wzorzec = re.escape(koncowka) + r"[.,;:!? ]*$"
    return [wiersz for wiersz in wiersze if re.search(wzorzec, wiersz)]


if __name__ == "__main__":
    n = int(input())
    wiersze = [input() for _ in range(n)]
    koncowka = input()

    wynik = wiersze_konczace_sie(wiersze, koncowka)
    if wynik:
        print("\n".join(wynik))
    else:
        print("Brak wierszy.")
