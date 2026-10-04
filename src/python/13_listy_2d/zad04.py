r"""
ZAD-04 — Dodawanie i odejmowanie macierzy

**Poziom:** ★☆☆
**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `A` i `B` o wymiarach `n×m`.

a) Wypisz ich sumę $A + B$.

b) Wypisz ich różnicę $A - B$ (pierwsza minus druga).

Element wyniku w wierszu `i` i kolumnie `j` to odpowiednio $A_{ij} + B_{ij}$ oraz $A_{ij} - B_{ij}$.

### Wejście

* 1. linia: `n` — liczba wierszy
* 2. linia: `m` — liczba kolumn
* następnie `n` linii macierzy `A` (po `m` liczb całkowitych)
* następnie `n` linii macierzy `B` (po `m` liczb całkowitych)

### Wyjście

Najpierw `n` linii sumy, zaraz po nich `n` linii różnicy (bez pustej linii i dodatkowych napisów między nimi).

### Ograniczenia

* `1 ≤ n, m ≤ 20`

### Przykład

**Wejście:**

```
2
2
1 2
-2 0
5 -3
1 7
```

**Wyjście:**

```
6 -1
-1 7
-4 5
-3 -7
```

"""


def suma_macierzy(macierz_a, macierz_b):
    """Zwraca sumę dwóch macierzy o tych samych wymiarach."""
    wynik = []
    for i in range(len(macierz_a)):
        wiersz = []
        for j in range(len(macierz_a[i])):
            wiersz.append(macierz_a[i][j] + macierz_b[i][j])
        wynik.append(wiersz)
    return wynik


def roznica_macierzy(macierz_a, macierz_b):
    """Zwraca różnicę macierz_a − macierz_b (macierze o tych samych wymiarach)."""
    wynik = []
    for i in range(len(macierz_a)):
        wiersz = []
        for j in range(len(macierz_a[i])):
            wiersz.append(macierz_a[i][j] - macierz_b[i][j])
        wynik.append(wiersz)
    return wynik


def wczytaj_macierz(liczba_wierszy):
    return [[int(x) for x in input().split()] for _ in range(liczba_wierszy)]


def wypisz_macierz(macierz):
    for wiersz in macierz:
        print(" ".join(str(x) for x in wiersz))


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    macierz_a = wczytaj_macierz(n)
    macierz_b = wczytaj_macierz(n)

    wypisz_macierz(suma_macierzy(macierz_a, macierz_b))
    wypisz_macierz(roznica_macierzy(macierz_a, macierz_b))
