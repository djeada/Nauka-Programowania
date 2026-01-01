"""
ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

* 1. linia: napis
* 2. linia: pojedynczy znak

### Wyjście

* 1. linia: liczba wystąpień

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

"""


def liczba_wystapien(napis, znak):
    return napis.count(znak)


def test_liczba_wystapien():
    assert liczba_wystapien("ala ma kota", "a") == 3
    assert liczba_wystapien("ala ma kota", "k") == 1


if __name__ == "__main__":

    test_liczba_wystapien()
