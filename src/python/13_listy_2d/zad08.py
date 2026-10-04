r"""
ZAD-08 — Wypisanie elementów macierzy spiralnie

**Poziom:** ★★☆
**Tagi:** `macierze`, `spirala`

### Treść

Wczytaj macierz `n×m` i wypisz jej elementy spiralnie, zgodnie z ruchem wskazówek zegara: zacznij od lewego górnego rogu, idź w prawo po pierwszym wierszu, potem w dół po ostatniej kolumnie, w lewo po ostatnim wierszu, w górę po pierwszej kolumnie i tak dalej, aż do odczytania wszystkich elementów.

### Wejście

* 1. linia: `n m` — liczba wierszy i kolumn (w jednej linii)
* następnie `n` linii po `m` liczb całkowitych

### Wyjście

Jedna linia: wszystkie elementy w kolejności spiralnej, oddzielone spacjami.

### Ograniczenia

* `1 ≤ n, m ≤ 20`

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

### Uwagi

* Macierz nie musi być kwadratowa — sprawdź swój program także dla jednego wiersza i dla jednej kolumny.

"""


def spirala(macierz):
    """Zwraca listę elementów macierzy odczytanych spiralnie, zgodnie z ruchem wskazówek zegara."""
    wynik = []
    gora, dol = 0, len(macierz) - 1
    lewo, prawo = 0, len(macierz[0]) - 1

    while gora <= dol and lewo <= prawo:
        # w prawo po górnym wierszu
        for j in range(lewo, prawo + 1):
            wynik.append(macierz[gora][j])
        gora += 1

        # w dół po prawej kolumnie
        for i in range(gora, dol + 1):
            wynik.append(macierz[i][prawo])
        prawo -= 1

        # w lewo po dolnym wierszu (jeśli jeszcze został)
        if gora <= dol:
            for j in range(prawo, lewo - 1, -1):
                wynik.append(macierz[dol][j])
            dol -= 1

        # w górę po lewej kolumnie (jeśli jeszcze została)
        if lewo <= prawo:
            for i in range(dol, gora - 1, -1):
                wynik.append(macierz[i][lewo])
            lewo += 1

    return wynik


if __name__ == "__main__":
    n, m = [int(x) for x in input().split()]
    macierz = [[int(x) for x in input().split()] for _ in range(n)]

    print(" ".join(str(x) for x in spirala(macierz)))
