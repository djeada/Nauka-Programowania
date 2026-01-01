"""
ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zamienia wartości miejscami i zwraca je jako parę `(b, a)`.

### Wejście

Dwa argumenty: `a`, `b` (liczby naturalne)

### Wyjście

Dwie liczby naturalne zwrócone jako krotka / para:

* najpierw nowa wartość `a` (czyli stare `b`)
* potem nowa wartość `b` (czyli stare `a`)

### Przykład

**Wywołanie funkcji:**

```python
a, b = zamien_wartosci(8, 5)
print("a =", a)
print("b =", b)
```

**Wyjście:**

```
a = 5
b = 8
```

"""


def swap(pierwsza_liczba, druga_liczba):
    """
    Funkcja zamienia wartosci miejscami.
    """
    return druga_liczba, pierwsza_liczba


def test_swap():
    a, b = 1, 2
    a, b = swap(a, b)
    assert a == 2 and b == 1


if __name__ == "__main__":
    test_swap()
