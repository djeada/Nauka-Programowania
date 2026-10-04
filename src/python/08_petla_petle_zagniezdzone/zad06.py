r"""
ZAD-06 — Litera Z

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj liczbę naturalną `n` i wypisz literę `Z` o wysokości i szerokości `n`:

* pierwszy i ostatni wiersz składają się z `n` gwiazdek,
* w pozostałych wierszach jest jedna gwiazdka leżąca na przekątnej biegnącej z prawego górnego do lewego dolnego rogu.

W wierszu `i` i kolumnie `j` (numerowanych od `0` do `n - 1`) wypisz `*`, gdy `i == 0`, `i == n - 1` lub `j == n - 1 - i`. W przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 3`)

### Wyjście

`n` linii z gwiazdkami i spacjami tworzących literę `Z`.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*****
   *
  *
 *
*****
```

"""


def litera_z(n):
    for i in range(n):
        wiersz = ""
        for j in range(n):
            if i == 0 or i == n - 1 or j == n - 1 - i:
                wiersz += "*"
            else:
                wiersz += " "
        print(wiersz.rstrip())


if __name__ == "__main__":
    n = int(input())
    litera_z(n)
