"""
ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `list`, `filter`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy, które występują również w drugiej liście.

* Zachowaj kolejność pozostałych elementów z pierwszej listy.
* Jeśli wszystko zostanie usunięte — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista 1 po usunięciu elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[9, 5]
```

"""


def usun_czesc_wspolna(lista_a, lista_b):
    for element in lista_a:
        if element in lista_b:
            lista_a.remove(element)
    return lista_a


def test_usun_czesc_wspolna():
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == []
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) == [5]
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 7]) == [5, 6, 7]


if __name__ == "__main__":

    test_usun_czesc_wspolna()
