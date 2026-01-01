"""
ZAD-06 — Histogram znaków w słowie

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Zwróć słownik: znak → liczba wystąpień.

### Wejście

* 1 linia: napis

### Wyjście

* Słownik, np. `{'k': 1, 'l': 1, 'a': 2, 's': 1}`

### Przykład

**Wejście:**

```
klasa
```

**Wyjście:**

```
{'k': 1, 'l': 1, 'a': 2, 's': 1}
```

"""


def histogram(napis):
    """
    Funkcja zwraca slownik zawierajacy wszystkie litery w napisie oraz czestosc ich wystepowania.
    """
    histogram = {}
    for znak in napis:
        if znak in histogram:
            histogram[znak] += 1
        else:
            histogram[znak] = 1
    return histogram


def test_histogram():
    assert histogram("") == {}
    assert histogram("ala") == {"a": 2, "l": 1}
    assert histogram("ala ma kota") == {
        "a": 4,
        " ": 2,
        "k": 1,
        "l": 1,
        "m": 1,
        "o": 1,
        "t": 1,
    }


if __name__ == "__main__":
    test_histogram()
