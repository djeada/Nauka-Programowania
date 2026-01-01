"""
ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe elementy dłuższej listy w tej samej kolejności.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**

### Przykład

**Wejście:**

```
[5, 3, 7, 2]
[1, -2, 3]
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

"""


def wypisz_na_przemian(lista_a, lista_b):

    min_dlugosc = min(len(lista_a), len(lista_b))

    for i in range(min_dlugosc):
        print(f"{lista_a[i]}, {lista_b[i]}", end=", ")

    for i in range(min_dlugosc, len(lista_a)):
        print(f"{lista_a[i]}, 0", end=", ")

    for i in range(min_dlugosc, len(lista_b)):
        print(f"0, {lista_b[i]}", end=", ")

    print()


if __name__ == "__main__":

    print("Podaj dlugosc pierwszej listy")
    dlugosc_a = int(input())

    print(f"Podaj {dlugosc_a} elementow:")
    lista_a = [int(input()) for i in range(dlugosc_a)]

    print("Podaj dlugosc drugiej listy")
    dlugosc_b = int(input())

    print(f"Podaj {dlugosc_b} elementow:")
    lista_b = [int(input()) for i in range(dlugosc_b)]

    wypisz_na_przemian(lista_a, lista_b)
