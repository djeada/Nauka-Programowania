"""
ZAD-08 — Indeks klucza w cyklicznie posortowanej liście

**Poziom:** ★★☆
**Tagi:** `binary search`, `rotacja`, `list`

### Treść

Otrzymujesz cyklicznie posortowaną listę liczb całkowitych (lista była rosnąca, ale została przesunięta) oraz klucz. Znajdź indeks **pierwszego** wystąpienia klucza. Jeśli klucza nie ma — wypisz `-1`.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb całkowitych oddzielonych spacjami
* 3 linia: liczba całkowita `x` (szukany klucz)

### Wyjście

* 1 linia: indeks pierwszego wystąpienia `x` albo `-1`

### Przykład

**Wejście:**

```
6
3 4 5 6 1 2
4
```

**Wyjście:**

```
1
```

### Ograniczenia / gwarancje

* Lista jest wynikiem rotacji listy posortowanej niemalejąco (mogą wystąpić duplikaty).

"""


def znajdz_klucz_v1(lista, klucz):

    lewo = 0
    prawo = len(lista) - 1

    while lewo <= prawo:

        sr = (lewo + prawo) // 2

        if klucz == lista[sr]:
            return sr

        if lista[sr] <= lista[prawo]:

            if lista[sr] < klucz and klucz <= lista[prawo]:
                lewo = sr + 1

            else:
                prawo = sr - 1

        else:

            if lista[lewo] <= klucz and klucz < lista[sr]:
                prawo = sr - 1

            else:
                lewo = sr + 1

    return -1


if __name__ == "__main__":

    lista = [27, 31, 32, 3, 5, 9, 10, 15]
    klucz = 31
    wynik = 1

    assert znajdz_klucz_v1(lista, klucz) == wynik

    lista = [4, 7, 12, 32, 51, 90, 100, 1, 2]
    klucz = -5
    wynik = -1

    assert znajdz_klucz_v1(lista, klucz) == wynik
