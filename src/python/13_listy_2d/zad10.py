"""
ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `n` wierszy obróconej macierzy

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

"""


def obroc_o_90(macierz):
    """
    Funkcja obraca macierz o 90 stopni zgodnie z ruchem wskazówek zegara.
    
    Złożoność czasowa: O(n²), gdzie n to rozmiar macierzy
    Złożoność pamięciowa: O(1) - obrót in-place
    """

    if len(macierz) != len(macierz[0]):
        raise ValueError("Macierz nie jest kwadratowa")

    n = len(macierz)

    # Obrót o 90 stopni w prawo: transpozycja + odwrócenie wierszy
    # Najpierw transpozycja
    for i in range(n):
        for j in range(i + 1, n):
            macierz[i][j], macierz[j][i] = macierz[j][i], macierz[i][j]
    
    # Potem odwrócenie każdego wiersza
    for i in range(n):
        macierz[i].reverse()

    return macierz


def test_obroc_o_90():
    macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    wynik = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert obroc_o_90(macierz) == wynik


if __name__ == "__main__":
    # Wczytanie rozmiaru macierzy
    n = int(input().strip())
    
    # Wczytanie macierzy
    macierz = []
    for _ in range(n):
        wiersz = list(map(int, input().strip().split()))
        macierz.append(wiersz)
    
    # Obrót macierzy o 90 stopni
    # Złożoność czasowa: O(n²)
    # Złożoność pamięciowa: O(1)
    obroc_o_90(macierz)
    
    # Wypisanie wyniku
    for wiersz in macierz:
        print(' '.join(map(str, wiersz)))
