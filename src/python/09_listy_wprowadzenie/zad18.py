"""
ZAD-18 — Indeks najmniejszego elementu w przesuniętej liście

**Poziom:** ★★☆
**Tagi:** `binarne`, `rotacja`, `minimum`

### Treść

Wczytaj listę liczb całkowitych, która była posortowana rosnąco i została przesunięta w prawo o nieznaną liczbę miejsc. Znajdź indeks najmniejszego elementu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — indeks najmniejszego elementu (od `0`).

### Przykład

**Wejście:**

```
5
7
8
-1
4
5
```

**Wyjście:**

```
2
```

"""


def znajdz_min_indeks(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return i + 1

    return 0


def test_znajdz_min_indeks():
    assert znajdz_min_indeks([7, 8, -1, 4, 5]) == 2
    assert znajdz_min_indeks([2, 3, 4, 5, 6]) == 0
    assert znajdz_min_indeks([8, 9, 10, 11, 1]) == 4


if __name__ == "__main__":

    test_znajdz_min_indeks()
