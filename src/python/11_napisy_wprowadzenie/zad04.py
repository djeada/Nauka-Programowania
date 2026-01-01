"""
ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `string`, `upper`

### Treść

Wczytaj napis i zamień wszystkie litery na wielkie.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po konwersji

### Przykład

**Wejście:**

```
Rumcajs
```

**Wyjście:**

```
RUMCAJS
```

"""


def na_male(napis):
    return napis.lower()


def test_na_male():
    assert na_male("test") == "test"
    assert na_male("Test") == "test"
    assert na_male("TEST") == "test"


if __name__ == "__main__":
    test_na_male()
