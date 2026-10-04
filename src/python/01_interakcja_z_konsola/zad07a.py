r"""
ZAD-07A — Pole trójkąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Wczytaj długość podstawy $a$ i wysokość $h$ trójkąta i oblicz jego pole ze wzoru $P = \frac{1}{2} a h$.

### Wejście

* 1. linia: `a` — liczba rzeczywista, $a > 0$
* 2. linia: `h` — liczba rzeczywista, $h > 0$

### Wyjście

Jedna linia: `P` do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
6
4
```

**Wyjście:**

```
12.000
```

"""


def pole_trojkata(a, h):
    return a * h / 2


if __name__ == "__main__":
    a = float(input())
    h = float(input())
    print(f"{pole_trojkata(a, h):.3f}")
