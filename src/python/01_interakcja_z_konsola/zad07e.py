r"""
ZAD-07E — Objętość stożka

**Poziom:** ★☆☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Wczytaj promień podstawy $r$ i wysokość $h$ stożka i oblicz jego objętość ze wzoru $V = \frac{1}{3}\pi r^2 h$.

### Wejście

* 1. linia: `r` — liczba rzeczywista, $r > 0$
* 2. linia: `h` — liczba rzeczywista, $h > 0$

### Wyjście

Jedna linia: `V` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
12.566
```

"""

import math


def objetosc_stozka(r, h):
    return math.pi * r**2 * h / 3


if __name__ == "__main__":
    r = float(input())
    h = float(input())
    print(f"{objetosc_stozka(r, h):.3f}")
