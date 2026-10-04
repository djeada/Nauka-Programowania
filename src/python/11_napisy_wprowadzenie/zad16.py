r"""
ZAD-16 — Odległość Hamminga

**Poziom:** ★★☆
**Tagi:** `napisy`, `porównywanie`, `pętle`

### Treść

Wczytaj dwa napisy tej samej długości i policz, na ilu pozycjach mają różne znaki (tzw. odległość Hamminga). Wielkość liter ma znaczenie.

### Wejście

* 1. linia: napis `s1` (bez spacji)
* 2. linia: napis `s2` (bez spacji, tej samej długości co `s1`)

### Wyjście

Jedna linia: odległość Hamminga.

### Przykład

**Wejście:**

```
adam
axam
```

**Wyjście:**

```
1
```

"""


def odleglosc_hamminga(napis_a, napis_b):
    licznik = 0
    for i in range(len(napis_a)):
        if napis_a[i] != napis_b[i]:
            licznik += 1
    return licznik


if __name__ == "__main__":
    napis_a = input()
    napis_b = input()
    print(odleglosc_hamminga(napis_a, napis_b))
