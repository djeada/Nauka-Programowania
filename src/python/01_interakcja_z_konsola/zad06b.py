r"""
ZAD-06B — Cale → centymetry

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj długość w calach `inch` i przelicz ją na centymetry: $cm = inch \cdot 2.54$.

### Wejście

* 1 linia: `inch` — liczba rzeczywista, $inch \ge 0$

### Wyjście

Jedna linia: `cm` do **2 miejsc po przecinku**.

### Przykład

**Wejście:**

```
10
```

**Wyjście:**

```
25.40
```

"""


def cale_na_centymetry(cale):
    return cale * 2.54


if __name__ == "__main__":
    cale = float(input())
    print(f"{cale_na_centymetry(cale):.2f}")
