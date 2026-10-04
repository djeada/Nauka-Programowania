r"""
ZAD-05 — Wyodrębnij cyfry z tekstu

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj tekst i wypisz wszystkie występujące w nim cyfry `0–9` sklejone w jeden napis, w kolejności występowania. Pozostałe znaki (także kropki i minusy w liczbach) pomiń.

### Wejście

* 1. linia: tekst

### Wyjście

* Jedna linia: cyfry z tekstu (z zachowaniem kolejności i zer na początku),
* `Brak cyfr.` — jeśli w tekście nie ma żadnej cyfry.

### Przykład

**Wejście:**

```
Terminator2001
```

**Wyjście:**

```
2001
```

### Uwagi

* Przydadzą się `re.findall(r"[0-9]", tekst)` albo `re.sub(r"[^0-9]", "", tekst)`.

"""

import re


def wyodrebnij_cyfry(tekst):
    return re.sub(r"[^0-9]", "", tekst)


if __name__ == "__main__":
    tekst = input()
    cyfry = wyodrebnij_cyfry(tekst)
    print(cyfry if cyfry else "Brak cyfr.")
