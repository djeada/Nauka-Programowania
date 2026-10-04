r"""
ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Wczytaj liczbę rzeczywistą $x$ (kąt w radianach) i oblicz:

$y = \sin^3(x) \cdot \cos^2(x) + e^{x^2} + \ln(x^3 + 2x^2 - x - 3)$

gdzie $\ln$ oznacza logarytm naturalny, a $e$ — podstawę logarytmu naturalnego.

### Wejście

* 1 linia: `x` — liczba zmiennoprzecinkowa (w radianach)

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $1.2 \le x \le 3$, więc spełniony jest warunek dziedziny logarytmu $x^3 + 2x^2 - x - 3 > 0$.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.126
```

### Uwagi

* Skorzystaj z modułu `math`: `math.sin`, `math.cos`, `math.exp`, `math.log` (logarytm naturalny).

"""

import math


def funkcja(x):
    return (
        math.sin(x) ** 3 * math.cos(x) ** 2
        + math.exp(x**2)
        + math.log(x**3 + 2 * x**2 - x - 3)
    )


if __name__ == "__main__":
    x = float(input())
    print(f"{funkcja(x):.3f}")
