"""
ZAD-06 — Sortowanie listy binarnej (0/1)

**Poziom:** ★★☆
**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Posortuj ją rosnąco.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb (0/1) oddzielonych spacjami

### Wyjście

* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

**Wejście:**

```
6
1 0 1 0 1 1
```

**Wyjście:**

```
[0, 0, 1, 1, 1, 1]
```

"""


def sortuj_tablice_binarna(lista):
    """
    Funkcja sortuje liste binarna.
    """
    zera = lista.count(0)

    for i in range(zera):
        lista[i] = 0

    for i in range(zera, len(lista)):
        lista[i] = 1

    return lista


def test_sortuj_binarna_tablice_v1():
    tablica = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
    oczekiwane = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    assert sortuj_tablice_binarna(tablica) == oczekiwane


if __name__ == "__main__":
    test_sortuj_binarna_tablice_v1()
