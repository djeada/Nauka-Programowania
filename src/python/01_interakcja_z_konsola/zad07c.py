r"""
ZAD-07C — Pole rombu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długości przekątnych rombu $d_1$ i $d_2$ i oblicz jego pole ze wzoru $P = \frac{1}{2} d_1 d_2$.

### Wejście

* 1. linia: `d1` — liczba rzeczywista, $d_1 > 0$
* 2. linia: `d2` — liczba rzeczywista, $d_2 > 0$

### Wyjście

Jedna linia: `P` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
10
6
```

**Wyjście:**

```
30.000
```

"""


def pole_rombu(d1, d2):
    return d1 * d2 / 2


if __name__ == "__main__":
    d1 = float(input())
    d2 = float(input())
    print(f"{pole_rombu(d1, d2):.3f}")
