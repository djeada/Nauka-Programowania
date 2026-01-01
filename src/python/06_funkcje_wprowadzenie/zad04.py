"""
ZAD-04A — Minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_dwoch(3, 1))
```

**Wyjście:**

```
1
```

ZAD-04B — Maksimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb naturalnych.

### Wejście

Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_dwoch(3, 1))
```

**Wyjście:**

```
3
```

ZAD-04C — Minimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `min`

### Treść

Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `min(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(min_z_trzech(3, 2, 1))
```

**Wyjście:**

```
1
```

ZAD-04D — Maksimum z trzech liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `max`

### Treść

Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.

### Wejście

Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)

### Wyjście

Funkcja zwraca:

* `max(a, b, c)`

### Przykład

**Wywołanie funkcji:**

```python
print(max_z_trzech(3, 2, 1))
```

**Wyjście:**

```
3
```

"""


def min_2(a, b):
    """
    Funkcja zwraca mniejsza z dwoch liczb.
    """
    if a < b:
        return a
    else:
        return b


def maks_2(a, b):
    """
    Funkcja zwraca wieksza z dwoch liczb.
    """
    if a > b:
        return a
    else:
        return b


def min_3(a, b, c):
    """
    Funkcja zwraca najmniejsza z trzech liczb.
    """
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


def maks_3(a, b, c):
    """
    Funkcja zwraca najwieksza z trzech liczb.
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def test_min_2():
    assert min_2(1, 2) == 1
    assert min_2(2, 1) == 1
    assert min_2(2, 2) == 2


def test_maks_2():
    assert maks_2(1, 2) == 2
    assert maks_2(2, 1) == 2
    assert maks_2(2, 2) == 2


def test_min_3():
    assert min_3(1, 2, 3) == 1
    assert min_3(2, 1, 3) == 1
    assert min_3(3, 1, 2) == 1
    assert min_3(2, 3, 1) == 1
    assert min_3(3, 2, 1) == 1
    assert min_3(1, 3, 2) == 1


def test_maks_3():
    assert maks_3(1, 2, 3) == 3
    assert maks_3(2, 1, 3) == 3
    assert maks_3(3, 1, 2) == 3
    assert maks_3(2, 3, 1) == 3
    assert maks_3(3, 2, 1) == 3
    assert maks_3(1, 3, 2) == 3


if __name__ == "__main__":

    test_min_2()
    test_maks_2()
    test_min_3()
    test_maks_3()
