"""
ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.

### Wejście

* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

* 1. linia: ciąg `1..n` bez spacji

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
123
```

"""


def liczby(n):
    napis = ""
    for i in range(1, n + 1):
        napis += str(i) + ", "
    return napis[:-2]


def test_liczby():
    assert liczby(-1) == ""
    assert liczby(5) == "1, 2, 3, 4, 5"


if __name__ == "__main__":

    test_liczby()
