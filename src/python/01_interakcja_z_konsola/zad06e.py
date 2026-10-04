r"""
ZAD-06E — Stopnie → radiany

**Poziom:** ★☆☆
**Tagi:** `pi`, `float`

### Treść

Wczytaj kąt w stopniach `deg` i przelicz go na radiany: $rad = \frac{deg \cdot \pi}{180}$.

### Wejście

* 1 linia: `deg` — liczba rzeczywista

### Wyjście

Jedna linia: `rad` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
180
```

**Wyjście:**

```
3.142
```

### Uwagi

* Wartość $\pi$ weź z modułu `math` (`math.pi`).

"""

import math


def stopnie_na_radiany(stopnie):
    return stopnie * math.pi / 180


if __name__ == "__main__":
    stopnie = float(input())
    print(f"{stopnie_na_radiany(stopnie):.3f}")
