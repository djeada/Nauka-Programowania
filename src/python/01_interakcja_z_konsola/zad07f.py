r"""
ZAD-07F — Objętość prostopadłościanu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długości krawędzi prostopadłościanu $a$, $b$, $c$ i oblicz jego objętość ze wzoru $V = a b c$.

### Wejście

* 1. linia: `a` — liczba rzeczywista, $a > 0$
* 2. linia: `b` — liczba rzeczywista, $b > 0$
* 3. linia: `c` — liczba rzeczywista, $c > 0$

### Wyjście

Jedna linia: `V` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
2
3
4
```

**Wyjście:**

```
24.000
```

"""


def objetosc_prostopadloscianu(a, b, c):
    return a * b * c


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    print(f"{objetosc_prostopadloscianu(a, b, c):.3f}")
