"""
ZAD-15 — Element dominujący

**Poziom:** ★★☆
**Tagi:** `zliczanie`, `dict`, `majority`

### Treść

Wczytaj listę liczb naturalnych. Jeśli istnieje liczba, która występuje **więcej niż N/2 razy**, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — element dominujący lub `-1`.

### Przykład

**Wejście:**

```
5
4
7
4
4
2
```

**Wyjście:**

```
4
```

"""


def element_dominujacy(lista):
    for element in lista:
        if lista.count(element) > len(lista) / 2:
            return element

    return -1


def test_element_dominujacy():
    assert element_dominujacy([]) == -1
    assert element_dominujacy([1]) == 1
    assert element_dominujacy([4, 7, 4, 4, 2]) == 4
    assert element_dominujacy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1


if __name__ == "__main__":

    test_element_dominujacy()
