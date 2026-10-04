r"""
ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` linii po `n` liczb całkowitych

### Wyjście

`n` linii obróconej macierzy.

### Ograniczenia

* `1 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

### Uwagi

* Pierwszy wiersz wyniku to pierwsza kolumna macierzy czytana od dołu do góry. Obrót można też uzyskać, transponując macierz i odwracając każdy jej wiersz.

"""


def obroc_o_90(macierz):
    """Zwraca nową macierz: kwadratową macierz obróconą o 90° zgodnie z ruchem wskazówek zegara."""
    n = len(macierz)
    wynik = []
    for i in range(n):
        wiersz = []
        # i-ty wiersz wyniku to i-ta kolumna oryginału czytana od dołu
        for j in range(n - 1, -1, -1):
            wiersz.append(macierz[j][i])
        wynik.append(wiersz)
    return wynik


if __name__ == "__main__":
    n = int(input())
    macierz = [[int(x) for x in input().split()] for _ in range(n)]

    for wiersz in obroc_o_90(macierz):
        print(" ".join(str(x) for x in wiersz))
