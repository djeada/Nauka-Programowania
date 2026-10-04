r"""
ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz macierz `n×n`, w której element w wierszu `i` i kolumnie `j` (indeksy od `0`) ma wartość $i \cdot j$, i wypisz ją.

### Wejście

* 1. linia: `n`

### Wyjście

`n` linii po `n` liczb oddzielonych spacjami.

### Ograniczenia

* `1 ≤ n ≤ 20`

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
    """Zwraca macierz n×n, w której element [i][j] jest równy i * j."""
    macierz = []
    for i in range(n):
        wiersz = []
        for j in range(n):
            wiersz.append(i * j)
        macierz.append(wiersz)
    return macierz


def wypisz_macierz(macierz):
    for wiersz in macierz:
        print(" ".join(str(x) for x in wiersz))


if __name__ == "__main__":
    n = int(input())
    wypisz_macierz(stworz_macierz(n))
