"""
ZAD-04 — Dodawanie i odejmowanie macierzy

**Poziom:** ★☆☆
**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `n×m`.
a) Wypisz ich sumę.
b) Wypisz różnicę: (pierwsza − druga).

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* potem `n` wierszy pierwszej macierzy (po `m` liczb)
* potem `n` wierszy drugiej macierzy (po `m` liczb)

### Wyjście

Najpierw `n` wierszy sumy, potem `n` wierszy różnicy (bez dodatkowych napisów).

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
    """
    Funkcja sumuje dwie macierze o rownych wymiarach i zwraca wynik.

    Złożoność czasowa: O(n * m), gdzie n to liczba wierszy, m to liczba kolumn
    Złożoność pamięciowa: O(n * m) dla wynikowej macierzy
    """

    if len(macierz_a) != len(macierz_b):
        raise ValueError("Macierze maja rozne wymiary!")
    macierz_c = []
    for i in range(len(macierz_a)):
        macierz_c.append([])
        for j in range(len(macierz_a[i])):
            macierz_c[i].append(macierz_a[i][j] + macierz_b[i][j])
    return macierz_c


def roznica_macierzy(macierz_a, macierz_b):
    """
    Funkcja odejmuje macierz_b od macierz_a i zwraca wynik.

    Złożoność czasowa: O(n * m)
    Złożoność pamięciowa: O(n * m)
    """

    if len(macierz_a) != len(macierz_b):
        raise ValueError("Macierze maja rozne wymiary!")
    macierz_c = []
    for i in range(len(macierz_a)):
        macierz_c.append([])
        for j in range(len(macierz_a[i])):
            macierz_c[i].append(macierz_a[i][j] - macierz_b[i][j])
    return macierz_c


def test_suma_macierzy():
    macierz_a = [[1, 2], [3, 4]]
    macierz_b = [[5, 6], [7, 8]]
    macierz_c = [[6, 8], [10, 12]]
    assert suma_macierzy(macierz_a, macierz_b) == macierz_c


def test_roznica_macierzy():
    macierz_a = [[1, 2], [3, 4]]
    macierz_b = [[5, 6], [7, 8]]
    macierz_c = [[-4, -4], [-4, -4]]
    assert roznica_macierzy(macierz_a, macierz_b) == macierz_c


if __name__ == "__main__":
    # Wczytanie wymiarów macierzy
    n = int(input().strip())
    m = int(input().strip())

    # Wczytanie pierwszej macierzy
    macierz_a = []
    for _ in range(n):
        wiersz = list(map(int, input().strip().split()))
        macierz_a.append(wiersz)

    # Wczytanie drugiej macierzy
    macierz_b = []
    for _ in range(n):
        wiersz = list(map(int, input().strip().split()))
        macierz_b.append(wiersz)

    # Obliczenie sumy i różnicy
    # Złożoność czasowa: O(n * m)
    # Złożoność pamięciowa: O(n * m)
    suma = suma_macierzy(macierz_a, macierz_b)
    roznica = roznica_macierzy(macierz_a, macierz_b)

    # Wypisanie sumy
    for wiersz in suma:
        print(" ".join(map(str, wiersz)))

    # Wypisanie różnicy
    for wiersz in roznica:
        print(" ".join(map(str, wiersz)))
