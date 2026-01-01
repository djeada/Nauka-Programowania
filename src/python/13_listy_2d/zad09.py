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
    """

    # throw exception if not square
    if len(macierz) != len(macierz[0]):
        raise Exception("Macierz nie jest kwadratowa")

    n = len(macierz)

    klepsydry = []
    for wiersz in range(n):
        for kolumna in range(n):
            if not (wiersz == 0 or wiersz == n - 1 or kolumna == 0 or kolumna == n - 1):
                suma = (
                    macierz[wiersz + 1][kolumna]
                    + macierz[wiersz + 1][kolumna - 1]
                    + macierz[wiersz + 1][kolumna + 1]
                )
                suma += macierz[wiersz][kolumna]
                suma += (
                    macierz[wiersz - 1][kolumna]
                    + macierz[wiersz - 1][kolumna - 1]
                    + macierz[wiersz - 1][kolumna + 1]
                )
                klepsydry.append(suma)

    return klepsydry


def najwieksza_klepsydra(macierz):
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

    test_najwieksza_klepsydra()
