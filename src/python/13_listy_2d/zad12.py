r"""
ZAD-12 — Transpozycja i mnożenie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `pętle zagnieżdżone`, `algebra`

### Treść

Wczytaj macierz `A` o wymiarach `n×m` i macierz `B` o wymiarach `r×p`.

a) Wypisz macierz transponowaną $A^T$ o wymiarach `m×n`: jej wiersz `j` to kolumna `j` macierzy `A`, czyli $A^T_{ji} = A_{ij}$.

b) Wypisz iloczyn $A \cdot B$ o wymiarach `n×p`, w którym $(A \cdot B)_{ij} = \sum_{k} A_{ik} \cdot B_{kj}$ — element w wierszu `i` i kolumnie `j` to suma iloczynów kolejnych elementów wiersza `i` macierzy `A` i kolumny `j` macierzy `B`. Iloczyn istnieje tylko wtedy, gdy liczba kolumn `A` jest równa liczbie wierszy `B` ($m = r$); w przeciwnym razie zamiast iloczynu wypisz `Niezgodne wymiary.`

### Wejście

* 1. linia: `n m` — wymiary macierzy `A`
* następnie `n` linii po `m` liczb całkowitych
* następnie linia `r p` — wymiary macierzy `B`
* następnie `r` linii po `p` liczb całkowitych

### Wyjście

Najpierw `m` linii macierzy $A^T$, zaraz po nich `n` linii iloczynu $A \cdot B$ albo jedna linia `Niezgodne wymiary.` (bez pustych linii między częściami).

### Ograniczenia

* `1 ≤ n, m, r, p ≤ 10`
* elementy macierzy mają wartość bezwzględną nie większą niż 100

### Przykład

**Wejście:**

```
2 3
1 2 3
4 5 6
3 2
7 8
9 10
11 12
```

**Wyjście:**

```
1 4
2 5
3 6
58 64
139 154
```

Na przykład $58 = 1 \cdot 7 + 2 \cdot 9 + 3 \cdot 11$ (pierwszy wiersz `A` i pierwsza kolumna `B`).

### Uwagi

* Mnożenie macierzy wymaga trzech zagnieżdżonych pętli: po wierszach `A`, po kolumnach `B` i po sumowanych elementach.
* Mnożenie macierzy nie jest przemienne — $A \cdot B$ zwykle różni się od $B \cdot A$, a jeden z tych iloczynów może w ogóle nie istnieć.

"""


def transponuj(macierz):
    """Zwraca macierz transponowaną: wiersz j wyniku to kolumna j macierzy."""
    wynik = []
    for j in range(len(macierz[0])):
        wiersz = []
        for i in range(len(macierz)):
            wiersz.append(macierz[i][j])
        wynik.append(wiersz)
    return wynik


def pomnoz(macierz_a, macierz_b):
    """
    Zwraca iloczyn macierzy A (n×m) i B (m×p) albo None,
    gdy liczba kolumn A różni się od liczby wierszy B.
    """
    if len(macierz_a[0]) != len(macierz_b):
        return None
    wynik = []
    for i in range(len(macierz_a)):
        wiersz = []
        for j in range(len(macierz_b[0])):
            suma = 0
            for k in range(len(macierz_b)):
                suma += macierz_a[i][k] * macierz_b[k][j]
            wiersz.append(suma)
        wynik.append(wiersz)
    return wynik


def wczytaj_macierz():
    liczba_wierszy, _ = [int(x) for x in input().split()]
    return [[int(x) for x in input().split()] for _ in range(liczba_wierszy)]


def wypisz_macierz(macierz):
    for wiersz in macierz:
        print(" ".join(str(x) for x in wiersz))


if __name__ == "__main__":
    macierz_a = wczytaj_macierz()
    macierz_b = wczytaj_macierz()

    wypisz_macierz(transponuj(macierz_a))
    iloczyn = pomnoz(macierz_a, macierz_b)
    if iloczyn is None:
        print("Niezgodne wymiary.")
    else:
        wypisz_macierz(iloczyn)
