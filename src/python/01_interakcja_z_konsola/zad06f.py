r"""
ZAD-06F — Fahrenheit → Celsius i Kelviny

**Poziom:** ★☆☆
**Tagi:** `konwersje`, `float`

### Treść

Wczytaj temperaturę w stopniach Fahrenheita $F$. Oblicz temperaturę w stopniach Celsjusza oraz w kelwinach:

* $C = \frac{5}{9} (F - 32)$
* $K = C + 273.15$

### Wejście

* 1 linia: `F` — liczba rzeczywista

### Wyjście

Dwie linie:

1. `C` do **3 miejsc po przecinku**,
2. `K` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
32
```

**Wyjście:**

```
0.000
273.150
```

### Uwagi

* `K` obliczaj z niezaokrąglonej wartości `C` — zaokrąglaj dopiero przy wypisywaniu.

"""


def fahrenheit_na_celsjusz(f):
    return 5 / 9 * (f - 32)


def celsjusz_na_kelwin(c):
    return c + 273.15


if __name__ == "__main__":
    f = float(input())
    c = fahrenheit_na_celsjusz(f)
    k = celsjusz_na_kelwin(c)
    print(f"{c:.3f}")
    print(f"{k:.3f}")
