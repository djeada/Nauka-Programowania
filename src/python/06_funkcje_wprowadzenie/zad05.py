r"""
ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zwraca dwie otrzymane wartości w odwróconej kolejności, czyli parę `(b, a)`.

Program wczytuje `a` i `b`, zamienia ich wartości instrukcją `a, b = zamien_wartosci(a, b)` i wypisuje nowe wartości zmiennych.

### Wejście

* 1. linia: liczba naturalna `a`
* 2. linia: liczba naturalna `b`

### Wyjście

Dwie linie w formacie:

```
a = <nowa wartość a>
b = <nowa wartość b>
```

Nowa wartość `a` to stara wartość `b` i odwrotnie.

### Przykład

**Wejście:**

```
8
5
```

**Wyjście:**

```
a = 5
b = 8
```

### Kod startowy

```python
def zamien_wartosci(a, b):
    pass


a = int(input())
b = int(input())
a, b = zamien_wartosci(a, b)
print("a =", a)
print("b =", b)
```

"""


def zamien_wartosci(a, b):
    """Zwraca otrzymane wartości w odwróconej kolejności."""
    return b, a


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    a, b = zamien_wartosci(a, b)
    print("a =", a)
    print("b =", b)
