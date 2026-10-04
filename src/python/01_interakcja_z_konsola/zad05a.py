r"""
ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Treść

Wczytaj liczbę rzeczywistą $x$ i oblicz wartość funkcji $y = 3x + 10$.

### Wejście

* 1 linia: `x` — liczba całkowita lub zmiennoprzecinkowa

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-1000 \le x \le 1000$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
19.000
```

"""


def funkcja_liniowa(x):
    return 3 * x + 10


if __name__ == "__main__":
    x = float(input())
    print(f"{funkcja_liniowa(x):.3f}")
