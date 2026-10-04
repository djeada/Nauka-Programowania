r"""
ZAD-07 — Zerowanie macierzy

**Poziom:** ★★☆
**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Dla każdego zera w **wejściowej** macierzy wyzeruj cały jego wiersz i całą jego kolumnę. Zera powstałe w trakcie zerowania nie powodują dalszego zerowania.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn (w jednej linii)
* następnie `n` linii po `m` liczb całkowitych

### Wyjście

`n` linii zmodyfikowanej macierzy.

### Ograniczenia

* `1 ≤ n, m ≤ 20`

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

### Uwagi

* Najpierw zapamiętaj, które wiersze i kolumny zawierają zero, a dopiero potem zeruj — inaczej wyzerujesz całą macierz.

"""


def wyzeruj_macierz(macierz):
    """
    Zeruje (w miejscu) każdy wiersz i każdą kolumnę, w których
    w oryginalnej macierzy występuje zero.
    """
    wiersze_do_wyzerowania = set()
    kolumny_do_wyzerowania = set()

    # Najpierw tylko zapamiętujemy położenie zer, żeby nowe zera
    # nie powodowały dalszego zerowania.
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == 0:
                wiersze_do_wyzerowania.add(i)
                kolumny_do_wyzerowania.add(j)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if i in wiersze_do_wyzerowania or j in kolumny_do_wyzerowania:
                macierz[i][j] = 0

    return macierz


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    macierz = [[int(x) for x in input().split()] for _ in range(n)]

    for wiersz in wyzeruj_macierz(macierz):
        print(" ".join(str(x) for x in wiersz))
