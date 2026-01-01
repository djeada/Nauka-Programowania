"""
ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która oblicza `a * b` używając **tylko dodawania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a * b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 2))
```

**Wyjście:**

```
6
```

ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która oblicza `a // b` używając **tylko odejmowania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a // b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 2))
```

**Wyjście:**

```
1
```

"""


def iloczyn(mnozna, mnoznik):

    znak = 1

    if mnozna < 0:
        znak = -1
        mnozna = -mnozna

    if mnoznik < 0:
        znak *= -1
        mnoznik = -mnoznik

    iloczyn = 0
    for i in range(mnozna):
        iloczyn += mnoznik
    return iloczyn * znak


def iloraz(dzielna, dzielnik):
    znak = 1

    if dzielna < 0:
        znak = -1
        dzielna = -dzielna

    if dzielnik < 0:
        znak *= -1
        dzielnik = -dzielnik

    iloraz = 0
    while dzielna >= dzielnik:
        dzielna -= dzielnik
        iloraz += 1
    return iloraz * znak


def test_iloczyn():
    assert iloczyn(5, 3) == 15
    assert iloczyn(2, 3) == 6
    assert iloczyn(-2, 3) == -6
    assert iloczyn(2, -3) == -6
    assert iloczyn(-2, -3) == 6


def test_iloraz():
    assert iloraz(5, 3) == 1
    assert iloraz(2, 3) == 0
    assert iloraz(-2, 3) == 0
    assert iloraz(6, -3) == -2
    assert iloraz(-2, -3) == 0


if __name__ == "__main__":
    test_iloczyn()
    test_iloraz()
