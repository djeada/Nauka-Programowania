"""
ZAD-04 — Minimum oraz maksimum

**Poziom:** ★☆☆
**Tagi:** `listy`, `min`, `max`

### Treść

Wczytaj `N` liczb całkowitych. Wypisz:

1. największą liczbę w liście
2. najmniejszą liczbę w liście

w jednej linii, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna linia:

* `max min`

### Przykład

**Wejście:**

```
9
4
-7
8
5
6
-9
10
2
-8
```

**Wyjście:**

```
10 -9
```

"""


def znajdz_maks(lista):
    maks = lista[0]
    for i in lista:
        if i > maks:
            maks = i
    return maks


def znajdz_min(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min


def test_znajdz_maks():
    assert znajdz_maks([5, 4, 3, 2, 1]) == 5
    assert znajdz_maks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10


def test_znajdz_min():
    assert znajdz_min([5, 4, 3, 2, 1]) == 1
    assert znajdz_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1


if __name__ == "__main__":

    test_znajdz_maks()
    test_znajdz_min()
