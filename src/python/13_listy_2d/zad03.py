"""
ZAD-03 — Macierz 2-kolumnowa z dwóch list

**Poziom:** ★☆☆
**Tagi:** `listy`, `macierze`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, wypisz macierz 2-kolumnową: wiersz `i` to `(lista1[i], lista2[i])`.
Jeśli długości są różne, wypisz: `Pusta macierz`

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Jeśli `n = m`: `n` wierszy `x y`
* Jeśli `n ≠ m`: jedna linia `Pusta macierz`

### Przykład

**Wejście:**

```
3
3
3
5
2
2
8
1
```

**Wyjście:**

```
3 2
5 8
2 1
```

"""

import string


def polacz_listy_w_macierz(lista_a, lista_b):
    """
    Funkcja zwraca macierz dwuwymiarowa, ktorej pierwsza kolumna sklada sie z
    elementow pierwszej listy, a druga kolumna elementow drugiej listy.
    Jesli otrzymane listy nie sa rownej dlugosci zwroc pusta macierz.
    """
    if len(lista_a) != len(lista_b):
        return []
    macierz = []
    for element_a, element_b in zip(lista_a, lista_b):
        macierz.append(element_a, element_b)
    return macierz


def test_polacz_listy_w_macierz():
    assert polacz_listy_w_macierz([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]
    assert polacz_listy_w_macierz([1, 2, 3], [4, 5]) == []


if __name__ == "__main__":
    test_polacz_listy_w_macierz()
