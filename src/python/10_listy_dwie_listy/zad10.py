"""
ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `list`, `median`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych:

* obie są posortowane rosnąco,
* obie mają tę samą, niezerową długość.

Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po „złączeniu” obu list).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: mediana jako liczba zmiennoprzecinkowa
  (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
4.5
```

"""


def mediana_list(lista_a, list_b):
    lista_a.extend(list_b)
    lista_a.sort()
    return lista_a[len(lista_a) // 2]


def test_mediana_list():
    assert mediana_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 7
    assert mediana_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]) == 8


if __name__ == "__main__":

    test_mediana_list()
