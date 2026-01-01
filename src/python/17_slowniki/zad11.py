"""
ZAD-11 — Sortowanie „słownika” po kluczach i po wartościach

**Poziom:** ★☆☆
**Tagi:** `sort`, `dict`

### Treść

Wczytaj `n` par `klucz wartość`.
a) Wypisz listę par posortowaną rosnąco po kluczach.
b) Wypisz listę par posortowaną rosnąco po wartościach.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`

### Wyjście

* 1 linia: lista par dla a)
* 2 linia: lista par dla b)

### Przykład

**Wejście:**

```
4
c 3
x 5
a -2
b 4
```

**Wyjście:**

```
[('a', -2), ('b', 4), ('c', 3), ('x', 5)]
[('a', -2), ('c', 3), ('b', 4), ('x', 5)]
```

"""


def sortuj_wzgledem_kluczy(slownik):
    """
    Funkcja sortuje slownik wzgledem kluczy.
    """
    return sorted(slownik.items(), key=lambda x: x[0])


def sortuj_wzgledem_wartosci(slownik):
    """
    Funkcja sortuje slownik wzgledem wartosci.
    """
    return sorted(slownik.items(), key=lambda x: x[1])


def test_sortuj_wzgledem_kluczy():
    assert sortuj_wzgledem_kluczy({"a": 2, "c": 1, "b": 3}) == [
        ("a", 2),
        ("b", 3),
        ("c", 1),
    ]


def test_sortuj_wzgledem_wartosci():
    assert sortuj_wzgledem_wartosci({"a": 2, "c": 1, "b": 3}) == [
        ("c", 1),
        ("a", 2),
        ("b", 3),
    ]


if __name__ == "__main__":

    test_sortuj_wzgledem_kluczy()
    test_sortuj_wzgledem_wartosci()
