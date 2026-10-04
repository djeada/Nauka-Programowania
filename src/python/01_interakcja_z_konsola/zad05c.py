r"""
ZAD-05C — Funkcja sześcienna: y = x³ + 2

**Poziom:** ★☆☆
**Tagi:** `potęgi`, `float`

### Treść

Wczytaj liczbę rzeczywistą $x$ i oblicz $y = x^3 + 2$.

### Wejście

* 1 linia: `x` — liczba rzeczywista

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-100 \le x \le 100$

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
127.000
```

"""


def funkcja_szescienna(x):
    return x**3 + 2


if __name__ == "__main__":
    x = float(input())
    print(f"{funkcja_szescienna(x):.3f}")
