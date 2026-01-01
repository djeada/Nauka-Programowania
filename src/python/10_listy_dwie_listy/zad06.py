"""
ZAD-06 — Znalezienie elementów wspólnych dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych. Wypisz listę elementów, które występują w obu listach:

* zachowaj **kolejność występowania w pierwszej liście**,
* jeśli element z pierwszej listy występuje w drugiej liście, dodaj go do wyniku,
* jeśli nie ma elementów wspólnych — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[2, 4]
```

"""


def czesc_wspolna(lista_a, lista_b):
    return [x for x in lista_a if x in lista_b]


def test_czesc_wspolna():
    assert set(czesc_wspolna([3, 6, 2, 7, 9], [4, 2, 3, 5, 6])) == set([3, 6, 2])
    assert set(czesc_wspolna([1, 2, 3, 4], [2, 3, 4, 5, 6])) == set([2, 3, 4])


if __name__ == "__main__":
    test_czesc_wspolna()
