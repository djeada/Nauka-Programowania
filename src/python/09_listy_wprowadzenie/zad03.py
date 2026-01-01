"""
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
-1
```

**Wyjście:**

```
2
```

"""


def znajdz_klucz(lista, klucz):

    for i in range(len(lista)):
        if lista[i] == klucz:
            return i
    return -1


def test_znajdz_klucz():
    assert znajdz_klucz([1, 2, 3, 4, 5], 5) == 4
    assert znajdz_klucz([1, 2, 3, 4, 5], 6) == -1


if __name__ == "__main__":

    test_znajdz_klucz()
