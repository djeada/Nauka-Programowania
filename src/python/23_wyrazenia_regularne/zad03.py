r"""
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Wczytaj napis i sprawdź, czy składa się **wyłącznie** z cyfr `0–9`. Każdy inny znak — spacja, minus, kropka, litera — sprawia, że odpowiedź to `Fałsz`.

### Wejście

* 1. linia: napis

### Wyjście

* `Prawda` — jeśli napis zawiera tylko cyfry `0–9`,
* `Fałsz` — w przeciwnym razie.

### Ograniczenia

* Napis ma od 1 do 100 znaków.

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

### Przykład 2

**Wejście:**

```
12a
```

**Wyjście:**

```
Fałsz
```

### Uwagi

* Użyj `re.fullmatch()` — `re.match()` sprawdza tylko początek napisu.
* W Pythonie `\d` dopasowuje także cyfry innych pism, np. arabskie `٣` albo cyfry pełnej szerokości `３`. Aby dopuścić tylko `0–9`, użyj klasy `[0-9]` (albo flagi `re.ASCII`).

"""

import re


def czy_same_cyfry(napis):
    # [0-9], a nie \d: \d pasuje też do cyfr innych pism, np. '٣'.
    return re.fullmatch(r"[0-9]+", napis) is not None


if __name__ == "__main__":
    napis = input()
    print("Prawda" if czy_same_cyfry(napis) else "Fałsz")
