"""
ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb

### Wyjście

* `n` wierszy zmodyfikowanej macierzy

### Przykład

**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

"""


def wyzeruj_macierz(macierz):
    """
    Funkcja zamienia wszystkie elementy w kolumnach i wierszach na zera
    jesli jeden z elementow jest rowny zero.
    
    Złożoność czasowa: O(n * m), gdzie n to liczba wierszy, m to liczba kolumn
    Złożoność pamięciowa: O(n + m) dla zbiorów wierszy i kolumn do wyzerowania
    """
    if not macierz or not macierz[0]:
        return macierz
    
    # Znajdź wszystkie pozycje zer
    wiersze_do_wyzerowania = set()
    kolumny_do_wyzerowania = set()
    
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == 0:
                wiersze_do_wyzerowania.add(i)
                kolumny_do_wyzerowania.add(j)
    
    # Wyzeruj odpowiednie wiersze i kolumny
    for i in wiersze_do_wyzerowania:
        for j in range(len(macierz[i])):
            macierz[i][j] = 0
    
    for j in kolumny_do_wyzerowania:
        for i in range(len(macierz)):
            macierz[i][j] = 0
    
    return macierz


def test_wyzeruj_macierz():
    assert wyzeruj_macierz([[1, 2, 3], [4, 0, 6], [7, 8, 9]]) == [
        [1, 0, 3],
        [0, 0, 0],
        [7, 0, 9],
    ]
    assert wyzeruj_macierz([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]


if __name__ == "__main__":
    # Wczytanie wymiarów macierzy
    n, m = map(int, input().strip().split())
    
    # Wczytanie macierzy
    macierz = []
    for _ in range(n):
        wiersz = list(map(int, input().strip().split()))
        macierz.append(wiersz)
    
    # Wyzerowanie macierzy
    # Złożoność czasowa: O(n * m)
    # Złożoność pamięciowa: O(n + m)
    wyzeruj_macierz(macierz)
    
    # Wypisanie wyniku
    for wiersz in macierz:
        print(' '.join(map(str, wiersz)))
