"""
ZAD-05 — Największy wspólny dzielnik (NWD)

**Poziom:** ★☆☆
**Tagi:** `Euklides`, `modulo`, `pętle`

### Treść

Napisz funkcję `nwd(a, b)`, która zwraca największy wspólny dzielnik dwóch liczb naturalnych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWD(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nwd(60, 45))
```

**Wyjście:**

```
15
```

"""


def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def test_nwd():
    assert nwd(12, 15) == 3
    assert nwd(15, 12) == 3
    assert nwd(9, 6) == 3
    assert nwd(6, 9) == 3


if __name__ == "__main__":
    test_nwd()
