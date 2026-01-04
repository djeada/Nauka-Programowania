"""
ZAD-03 — Sortowanie przez wstawianie

**Poziom:** ★★☆
**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wstawianie**.
Buduj posortowany fragment od lewej strony: każdy kolejny element „wstaw” w odpowiednie miejsce, przesuwając większe elementy w prawo.

### Wejście

* 1 linia: lista liczb całkowitych

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

* Działa bardzo dobrze dla danych prawie posortowanych.

"""


def sortuj_v1(tablica):

    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1

        while j >= 0 and tablica[j] > klucz:
            tablica[j + 1] = tablica[j]
            j -= 1

        tablica[j + 1] = klucz


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
