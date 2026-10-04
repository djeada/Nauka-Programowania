r"""
ZAD-07D — Objętość kuli

**Poziom:** ★☆☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Wczytaj promień kuli $r$ i oblicz jej objętość ze wzoru $V = \frac{4}{3}\pi r^3$.

### Wejście

* 1 linia: `r` — liczba rzeczywista, $r > 0$

### Wyjście

Jedna linia: `V` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
1
```

**Wyjście:**

```
4.189
```

"""

import math


def objetosc_kuli(r):
    return 4 / 3 * math.pi * r**3


if __name__ == "__main__":
    r = float(input())
    print(f"{objetosc_kuli(r):.3f}")
