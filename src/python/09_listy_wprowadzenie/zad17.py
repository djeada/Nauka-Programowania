"""
ZAD-17 — Wszystkie pary o sumie x (wartości)

**Poziom:** ★★☆
**Tagi:** `listy`, `2-sum`, `pary`

### Treść

Wczytaj listę liczb całkowitych oraz `x`. Wypisz wszystkie pary **wartości** `(a, b)` z listy (nie indeksy), takie że `a + b == x`. Każdą parę wypisz w osobnej linii jako:
`a b`

Każdą parę wypisz tylko raz (nie dubluj `(a,b)` i `(b,a)`).

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Wiele linii — po jednej parze na linię.
Jeśli brak par — brak wyjścia.

### Przykład

**Wejście:**

```
5
1
2
4
3
7
5
```

**Wyjście:**

```
1 4
2 3
```

"""


def znajdz_pary(lista, x):
    wynik = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                wynik.append((i, j))
    return wynik


def test_znajdz_pary():
    assert znajdz_pary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [
        (0, 8),
        (1, 7),
        (2, 6),
        (3, 5),
    ]
    assert znajdz_pary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20) == []


if __name__ == "__main__":

    test_znajdz_pary()
