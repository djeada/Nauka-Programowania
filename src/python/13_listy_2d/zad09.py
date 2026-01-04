"""
ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):

```
a b c
  d
e f g
```

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb całkowitych

### Wyjście

* 1 linia: maksymalna suma klepsydry

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

"""


def znajdz_klepsydry(macierz):
    """
    Przejdz przez macierz i znajdz wszystkie klepsydry.

    Złożoność czasowa: O(n * m), gdzie n to liczba wierszy, m to liczba kolumn
    Złożoność pamięciowa: O((n-2) * (m-2)) dla wyników
    """
    n = len(macierz)
    m = len(macierz[0])

    klepsydry = []
    # Klepsydra potrzebuje 3x3, więc iterujemy od 1 do n-2 i m-2
    for wiersz in range(1, n - 1):
        for kolumna in range(1, m - 1):
            # Suma klepsydry:
            # wiersz-1: kolumna-1, kolumna, kolumna+1
            # wiersz: kolumna
            # wiersz+1: kolumna-1, kolumna, kolumna+1
            suma = (
                macierz[wiersz - 1][kolumna - 1]
                + macierz[wiersz - 1][kolumna]
                + macierz[wiersz - 1][kolumna + 1]
                + macierz[wiersz][kolumna]
                + macierz[wiersz + 1][kolumna - 1]
                + macierz[wiersz + 1][kolumna]
                + macierz[wiersz + 1][kolumna + 1]
            )
            klepsydry.append(suma)

    return klepsydry


def najwieksza_klepsydra(macierz):
    """
    Zwraca największą sumę klepsydry w macierzy.

    Złożoność czasowa: O(n * m)
    Złożoność pamięciowa: O((n-2) * (m-2))
    """
    return max(znajdz_klepsydry(macierz))


def test_najwieksza_klepsydra():

    macierz = [
        [10, 99, 28, 21, 78],
        [35, 78, 31, 56, 24],
        [7, 18, 2, 50, 87],
        [59, 67, 9, 82, 53],
        [23, 26, 76, 62, 36],
    ]
    assert najwieksza_klepsydra(macierz) == 395


if __name__ == "__main__":
    # Wczytanie wymiarów macierzy
    n, m = map(int, input().strip().split())

    # Wczytanie macierzy
    macierz = []
    for _ in range(n):
        wiersz = list(map(int, input().strip().split()))
        macierz.append(wiersz)

    # Znalezienie największej klepsydry
    # Złożoność czasowa: O(n * m)
    # Złożoność pamięciowa: O((n-2) * (m-2))
    wynik = najwieksza_klepsydra(macierz)

    # Wypisanie wyniku
    print(wynik)
