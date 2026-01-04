"""
ZAD-08 — Wypisanie elementów macierzy spiralnie

**Poziom:** ★★☆
**Tagi:** `macierze`, `spirala`

### Treść

Wczytaj macierz `n×m` i wypisz jej elementy spiralnie (zgodnie z ruchem wskazówek zegara), startując z lewego górnego rogu.

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* 1 linia: elementy spiralnie, oddzielone spacjami

### Przykład

**Wejście:**

```
3 3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
1 2 3 6 9 8 7 4 5
```

"""


def spirala(macierz):
    """
    Zwraca liste elementow z macierzy zebranych spiralnie.

    Złożoność czasowa: O(n * m), gdzie n to liczba wierszy, m to liczba kolumn
    Złożoność pamięciowa: O(n * m) dla wyniku
    """
    if not macierz or not macierz[0]:
        return []

    lista = []
    gora, dol = 0, len(macierz) - 1
    lewo, prawo = 0, len(macierz[0]) - 1

    while gora <= dol and lewo <= prawo:
        # Przejdź w prawo po górnym wierszu
        for j in range(lewo, prawo + 1):
            lista.append(macierz[gora][j])
        gora += 1

        # Przejdź w dół po prawej kolumnie
        for i in range(gora, dol + 1):
            lista.append(macierz[i][prawo])
        prawo -= 1

        # Przejdź w lewo po dolnym wierszu (jeśli jeszcze istnieje)
        if gora <= dol:
            for j in range(prawo, lewo - 1, -1):
                lista.append(macierz[dol][j])
            dol -= 1

        # Przejdź w górę po lewej kolumnie (jeśli jeszcze istnieje)
        if lewo <= prawo:
            for i in range(dol, gora - 1, -1):
                lista.append(macierz[i][lewo])
            lewo += 1

    return lista


def test_spirala():
    macierz = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]
    wynik = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    assert spirala(macierz) == wynik


if __name__ == "__main__":
    # Wczytanie wymiarów macierzy
    n, m = map(int, input().strip().split())

    # Wczytanie macierzy
    macierz = []
    for _ in range(n):
        wiersz = list(map(int, input().strip().split()))
        macierz.append(wiersz)

    # Spiralne przejście
    # Złożoność czasowa: O(n * m)
    # Złożoność pamięciowa: O(n * m)
    wynik = spirala(macierz)

    # Wypisanie wyniku
    print(" ".join(map(str, wynik)))
