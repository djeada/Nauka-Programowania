"""
ZAD-04 — Obliczanie silni liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `silnia`, `mnożenie`

### Treść

Napisz funkcję `silnia(n)`, która zwraca `n!` obliczone przy użyciu pętli.
Przyjmij, że `0! = 1`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `n!`.

### Przykład

**Wywołanie funkcji:**

```python
print(silnia(3))
```

**Wyjście:**

```
6
```

"""


def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(4) == 24
    assert silnia(5) == 120


if __name__ == "__main__":

    test_silnia()
