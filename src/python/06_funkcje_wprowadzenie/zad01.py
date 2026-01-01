"""
ZAD-01A — Zwracanie stałej wartości: liczba 3

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `int`

### Treść

Napisz funkcję (bez argumentów), która zwraca liczbę całkowitą `3`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `3`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_liczbe()
print(wynik)
```

**Wyjście:**

```
3
```

ZAD-01B — Zwracanie stałej wartości: napis „Tak”

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `string`

### Treść

Napisz funkcję (bez argumentów), która zwraca napis `Tak`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `Tak`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_napis()
print(wynik)
```

**Wyjście:**

```
Tak
```

ZAD-01C — Zwracanie stałej wartości: True

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `bool`

### Treść

Napisz funkcję (bez argumentów), która zwraca wartość logiczną `True`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `True`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_prawda()
print(wynik)
```

**Wyjście:**

```
True
```

"""


def zwroc_3():
    """
    Funkcja zwraca liczbe 3.
    """
    return 3


def zwroc_tak():
    """
    Funkcja zwraca napis "Tak".
    """
    return "Tak"


def zwroc_prawda():
    """
    Funkcja zwraca wartosc logiczna Prawda.
    """
    return True


def test_zwroc_3():
    assert zwroc_3() == 3


def test_zwroc_tak():
    assert zwroc_tak() == "Tak"


def test_zwroc_prawda():
    assert zwroc_prawda() == True


if __name__ == "__main__":

    test_zwroc_3()
    test_zwroc_tak()
    test_zwroc_prawda()
