r"""
ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `listy`, `iteracja`, `indeksy`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy element listy 1, pierwszy element listy 2, drugi element listy 1, drugi element listy 2 itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy wypisz pozostałe elementy dłuższej listy w ich kolejności.

### Wejście

* 1. linia: lista 1 — liczby całkowite oddzielone spacjami
* 2. linia: lista 2 — liczby całkowite oddzielone spacjami

### Wyjście

Jedna linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**.

### Przykład

**Wejście:**

```
5 3 7 2
1 -2 3
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

"""


def na_przemian(lista_a, lista_b):
    wynik = []
    for i in range(max(len(lista_a), len(lista_b))):
        if i < len(lista_a):
            wynik.append(lista_a[i])
        if i < len(lista_b):
            wynik.append(lista_b[i])
    return wynik


if __name__ == "__main__":
    lista_a = [int(x) for x in input().split()]
    lista_b = [int(x) for x in input().split()]

    wynik = na_przemian(lista_a, lista_b)
    print(*wynik, sep=",")
