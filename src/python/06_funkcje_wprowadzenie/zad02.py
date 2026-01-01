"""
ZAD-02A — Suma dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `suma(a, b)`, która zwraca sumę dwóch liczb całkowitych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita)
* `b` (liczba całkowita)

### Wyjście

Funkcja zwraca:

* `a + b`

### Przykład

**Wywołanie funkcji:**

```python
print(suma(3, 5))
```

**Wyjście:**

```
8
```

ZAD-02B — Różnica: b − a

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `roznica(a, b)`, która zwraca różnicę: `b - a`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `b - a`

### Przykład

**Wywołanie funkcji:**

```python
print(roznica(3, 5))
```

**Wyjście:**

```
2
```

ZAD-02C — Iloczyn dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn `a * b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `a * b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 5))
```

**Wyjście:**

```
15
```

ZAD-02D — Iloraz całkowity: a // b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `dzielenie`, `//`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a // b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 5))
```

**Wyjście:**

```
0
```

ZAD-02E — Reszta z dzielenia: a % b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `modulo`, `%`

### Treść

Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a % b`

### Przykład

**Wywołanie funkcji:**

```python
print(reszta(3, 5))
```

**Wyjście:**

```
3
```

"""


def suma(pierwsza_liczba, druga_liczba):
    """
    Funkcja zwraca sume dwoch liczb.
    """
    return pierwsza_liczba + druga_liczba


def roznica(pierwsza_liczba, druga_liczba):
    """
    Funkcja zwraca roznice dwoch liczb.
    """
    return pierwsza_liczba - druga_liczba


def iloczyn(pierwsza_liczba, druga_liczba):
    """
    Funkcja zwraca iloczyn dwoch liczb.
    """
    return pierwsza_liczba * druga_liczba


def iloraz(pierwsza_liczba, druga_liczba):
    """
    Funkcja zwraca iloraz dwoch liczb.
    """
    return pierwsza_liczba / druga_liczba


def reszta(pierwsza_liczba, druga_liczba):
    """
    Funkcja zwraca reszte z dzielenia pierwszej przez druga.
    """
    return pierwsza_liczba % druga_liczba


def test_suma():
    assert suma(2, 3) == 5


def test_roznica():
    assert roznica(2, 3) == -1


def test_iloczyn():
    assert iloczyn(2, 3) == 6


def test_iloraz():
    assert iloraz(9, 3) == 3


def test_reszta():
    assert reszta(9, 3) == 0


if __name__ == "__main__":

    test_suma()
    test_roznica()
    test_iloczyn()
    test_iloraz()
    test_reszta()
