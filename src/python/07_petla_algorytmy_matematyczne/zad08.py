"""
ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

* `True` lub `False`

### Przykład

**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

**Wyjście:**

```
True
False
```

### Uwagi

* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

"""

import math


def podziel(a, b):

    znak = 1

    if b == 0:
        return float("nan")

    if a == 0:
        return 0

    if a < 0:
        znak = -1
        a = -a

    if b < 0:
        znak *= -1
        b = -b

    if znak == 1:
        licznik = 0
        while a >= b:
            a -= b
            licznik += 1

    else:
        licznik = 1
        while a > b:
            a -= b
            licznik += 1

    return licznik * znak


def test_podziel():
    assert podziel(10, 2) == 5
    assert podziel(10, 3) == 3
    assert podziel(25, -5) == -5
    assert podziel(-25, 5) == -5
    assert podziel(-25, -5) == 5
    assert podziel(0, 5) == 0
    assert math.isnan(podziel(0, 0))


if __name__ == "__main__":

    test_podziel()
