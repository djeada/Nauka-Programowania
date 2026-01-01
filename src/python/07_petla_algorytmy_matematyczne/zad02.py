"""
ZAD-02 — Potęgowanie liczby przy pomocy pętli

**Poziom:** ★☆☆
**Tagi:** `pętle`, `potęgowanie`, `mnożenie`

### Treść

Napisz funkcję `potega(a, b)`, która oblicza `a^b` przy użyciu pętli (bez operatora potęgowania).

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — wartość `a^b`.

### Przykład

**Wywołanie funkcji:**

```python
print(potega(3, 5))
```

**Wyjście:**

```
243
```

### Uwagi o formatowaniu

* Dla `b = 0` wynik ma wynosić `1`.

"""


def potega(podstawa, wykladnik):
    wynik = 1
    for i in range(wykladnik):
        wynik *= podstawa
    return wynik


def test_potega():
    assert potega(2, 3) == 8
    assert potega(3, 2) == 9
    assert potega(4, 4) == 256
    assert potega(5, 3) == 125
    assert potega(6, 0) == 1
    assert potega(7, 1) == 7
    assert potega(0, 2) == 0


if __name__ == "__main__":

    test_potega()
