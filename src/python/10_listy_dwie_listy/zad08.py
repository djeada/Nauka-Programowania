"""
ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `list`, `merge`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w jedną listę:

* wynik ma być posortowany rosnąco,
* wynik ma zawierać **unikalne** elementy (bez duplikatów).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

"""


def polacz_posortowane_listy(lista_a, lista_b):
    lista_c = []
    while lista_a and lista_b:
        if lista_a[0] < lista_b[0]:
            lista_c.append(lista_a.pop(0))
        else:
            lista_c.append(lista_b.pop(0))
    lista_c.extend(lista_a)
    lista_c.extend(lista_b)
    return lista_c


def test_polacz_posortowane_listy():
    assert polacz_posortowane_listy([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert polacz_posortowane_listy([1, 3, 5], []) == [1, 3, 5]
    assert polacz_posortowane_listy([], [1, 3, 5]) == [1, 3, 5]
    assert polacz_posortowane_listy([], []) == []


if __name__ == "__main__":

    test_polacz_posortowane_listy()
