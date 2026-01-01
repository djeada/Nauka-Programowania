"""
ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej** pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

**Wejście:**

```
5
1
3
4
5
2
5
```

**Wyjście:**

```
0 2
```

"""


def znajdz_pare(lista, x):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                return i, j
    return -1, -1


def test_znajdz_pare():
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == (0, 8)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 22) == (-1, -1)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == (0, 6)
    assert znajdz_pare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == (-1, -1)


if __name__ == "__main__":

    test_znajdz_pare()
