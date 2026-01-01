"""
ZAD-01 — Sortowanie bąbelkowe

**Poziom:** ★☆☆
**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania bąbelkowego**.
Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów i zamianie ich miejscami, jeśli są w złej kolejności. Powtarzaj przebiegi, aż w całym przebiegu nie zajdzie żadna zamiana.

### Wejście

* 1 linia: lista liczb całkowitych, np. `[6, 2, 1, 4, 27]`

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Po każdym pełnym przebiegu największy element „wypływa” na koniec.
* W kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1.

"""


# Zlozonosc czasowa O(n^2)
def sortuj_v1(tablica):

    n = len(tablica)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]


# Testy Poprawnosci
def test_1():
    tablica = [4, 2, 5, 3, 1]
    wynik = [1, 2, 3, 4, 5]

    sortuj_v1(tablica)

    assert tablica == wynik


def test_2():
    tablica = [6, 5, 1, 2, 3, 1, 4, 3, 5, 2, 3]
    wynik = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

    sortuj_v1(tablica)

    assert tablica == wynik


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()
