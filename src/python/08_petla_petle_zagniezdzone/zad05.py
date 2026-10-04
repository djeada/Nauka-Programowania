r"""
ZAD-05 — Litera X

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `warunki`, `ASCII-art`

### Treść

Wczytaj liczbę naturalną `n` i wypisz literę `X` o wysokości i szerokości `n`, zbudowaną z gwiazdek leżących na obu przekątnych kwadratu.

W wierszu `i` i kolumnie `j` (numerowanych od `0` do `n - 1`) wypisz `*`, gdy `j == i` **lub** `j == n - 1 - i`. W przeciwnym razie wypisz spację.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 3`)

### Wyjście

`n` linii z gwiazdkami i spacjami tworzących literę `X`.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
*   *
 * *
  *
 * *
*   *
```

### Uwagi

* Dla parzystego `n` przekątne nie przecinają się w jednym punkcie — w dwóch środkowych wierszach gwiazdki stoją obok siebie.

"""


def litera_x(n):
    for i in range(n):
        wiersz = ""
        for j in range(n):
            if j == i or j == n - 1 - i:
                wiersz += "*"
            else:
                wiersz += " "
        print(wiersz.rstrip())


if __name__ == "__main__":
    n = int(input())
    litera_x(n)
