"""
ZAD-06 — Suma cyfr liczby (funkcja)

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `pętle`, `modulo`

### Treść

Napisz funkcję `suma_cyfr(n)`, która zwraca sumę cyfr liczby naturalnej `n`.

### Wejście

Jeden argument: `n` (`n ≥ 0`)

### Wyjście

Funkcja zwraca sumę cyfr.

### Przykład

**Wywołanie funkcji:**

```python
print(suma_cyfr(13231))
```

**Wyjście:**

```
10
```

### Uwagi

* Dla `n = 0` suma cyfr to `0`.

"""


def suma_cyfr(liczba):
    """
    Funkcja zwraca sume cyfr podanej liczby.
    """
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma


def test_suma_cyfr_dla_liczby_123():
    assert suma_cyfr(123) == 6


def test_suma_cyfr_dla_liczby_0():
    assert suma_cyfr(0) == 0


if __name__ == "__main__":

    test_suma_cyfr_dla_liczby_0()
    test_suma_cyfr_dla_liczby_123()
