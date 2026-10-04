r"""
ZAD-07B — Pole prostokąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długości boków prostokąta $a$ i $b$ i oblicz jego pole ze wzoru $P = a b$.

### Wejście

* 1. linia: `a` — liczba rzeczywista, $a > 0$
* 2. linia: `b` — liczba rzeczywista, $b > 0$

### Wyjście

Jedna linia: `P` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
2.5
4
```

**Wyjście:**

```
10.000
```

"""


def pole_prostokata(a, b):
    return a * b


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    print(f"{pole_prostokata(a, b):.3f}")
