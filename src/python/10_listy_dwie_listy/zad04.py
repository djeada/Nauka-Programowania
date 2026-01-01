"""
ZAD-04 — Iloczyn skalarny dwóch wektorów 3D

**Poziom:** ★☆☆
**Tagi:** `list`, `wektory`, `math`

### Treść

Wczytaj dwie listy długości 3 (wektory 3D) i oblicz ich **iloczyn skalarny**:
[
A_xB_x + A_yB_y + A_zB_z
]

### Wejście

* 1 linia: wektor A (lista 3 liczb całkowitych)
* 2 linia: wektor B (lista 3 liczb całkowitych)

### Wyjście

* 1 linia: jedna liczba całkowita — iloczyn skalarny

### Przykład

**Wejście:**

```
[1, 2, 3]
[3, 1, 2]
```

**Wyjście:**

```
11
```

"""


def iloczyn_wektorowy(lista_a, lista_b):

    if len(lista_a) != len(lista_b):
        print(
            "Nie mozna obliczyc iloczynu wektorowego, poniewaz listy nie maja takiej samej dlugosci"
        )
        return
    if len(lista_a) != 3:
        print(
            "Nie mozna obliczyc iloczynu wektorowego, poniewaz listy nie sa 3-wymiarowe"
        )
        return

    wynik = (
        lista_a[1] * lista_b[2] - lista_a[2] * lista_b[1],
        lista_a[2] * lista_b[0] - lista_a[0] * lista_b[2],
        lista_a[0] * lista_b[1] - lista_a[1] * lista_b[0],
    )
    return list(wynik)


def test_iloczyn_wektorowy():

    assert iloczyn_wektorowy([1, 2, 3], [4, 5, 6]) == [-3, 6, -3]
    assert iloczyn_wektorowy([0, -5, 8], [3, 7, -2]) == [-46, 24, 15]


if __name__ == "__main__":

    test_iloczyn_wektorowy()
