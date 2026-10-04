r"""
ZAD-05B — Funkcja liniowa: y = ax + b

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `float`

### Treść

Wczytaj współczynniki $a$, $b$ oraz argument $x$ i oblicz wartość funkcji liniowej $y = ax + b$.

### Wejście

3 liczby rzeczywiste, każda w osobnej linii:

* 1. linia: `a`
* 2. linia: `b`
* 3. linia: `x`

### Wyjście

Jedna linia: `y` do **3 miejsc po przecinku**.

### Ograniczenia

* $-1000 \le a, b, x \le 1000$

### Przykład

**Wejście:**

```
1
2
3
```

**Wyjście:**

```
5.000
```

"""


def funkcja_liniowa(a, b, x):
    return a * x + b


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    x = float(input())
    print(f"{funkcja_liniowa(a, b, x):.3f}")
