"""
ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od 0) ma wartość `i*j`.

### Wejście

* 1. linia: `n`

### Wyjście

* `n` wierszy po `n` liczb

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

"""


def stworz_macierz(n):
    """
    Funkcja tworzy macierz o wymiarach n x n, dla ktorej kazdy
    element jest rowny iloczynowi wspolrzednych (indeksów).

    Złożoność czasowa: O(n²)
    Złożoność pamięciowa: O(n²)
    """
    macierz = []
    for i in range(n):
        macierz.append([])
        for j in range(n):
            macierz[i].append(i * j)
    return macierz


def test_stworz_macierz():
    assert stworz_macierz(3) == [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
    assert stworz_macierz(4) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]


if __name__ == "__main__":
    # Wczytanie wartości n z wejścia
    n = int(input().strip())

    # Utworzenie macierzy
    # Złożoność czasowa: O(n²)
    # Złożoność pamięciowa: O(n²)
    macierz = stworz_macierz(n)

    # Wypisanie macierzy
    for wiersz in macierz:
        print(" ".join(map(str, wiersz)))
