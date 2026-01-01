"""
ZAD-03 — Suma elementów dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i zwróć listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
Jeśli któraś lista jest krótsza, brakujące elementy traktuj jako `0`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista sum

### Przykład

**Wejście:**

```
[3, 1, 2, 5]
[2, 8, 6, 5]
```

**Wyjście:**

```
[5, 9, 8, 10]
```

"""


def suma_list(lista_a, lista_b):
    if len(lista_a) > len(lista_b):
        lista_b = lista_b + [0] * (len(lista_a) - len(lista_b))
    elif len(lista_a) < len(lista_b):
        lista_a = lista_a + [0] * (len(lista_b) - len(lista_a))
    return [a + b for a, b in zip(lista_a, lista_b)]


def test_suma_list():
    assert suma_list([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert suma_list([1, 2, 3], [4, 5]) == [5, 7, 3]


if __name__ == "__main__":

    test_suma_list()
