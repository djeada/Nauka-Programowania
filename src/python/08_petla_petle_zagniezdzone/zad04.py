r"""
ZAD-04 — Tabliczka mnożenia N × N

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `formatowanie`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `N` i wypisz tabliczkę mnożenia o wymiarach `N × N`: w wierszu `i` i kolumnie `j` (licząc od `1`) ma znaleźć się iloczyn $i \cdot j$.

Aby kolumny tworzyły równą tabelę, każdą liczbę wyrównaj do prawej w polu o szerokości `w`, gdzie `w` to liczba cyfr największej liczby w tabeli, czyli `w = len(str(N * N))`. Kolejne pola w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `N` — liczba naturalna (`N ≥ 1`)

### Wyjście

`N` linii; w każdej `N` pól o szerokości `w` (liczba wyrównana do prawej, z lewej uzupełniona spacjami), oddzielonych pojedynczą spacją.

### Ograniczenia

* `1 ≤ N ≤ 30`

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
 1  2  3  4
 2  4  6  8
 3  6  9 12
 4  8 12 16
```

Największa liczba to `16`, więc `w = 2`: liczby jednocyfrowe są poprzedzone dodatkową spacją.

### Uwagi

* Zapis `f"{x:>{w}}"` w f-stringu wypisuje `x` wyrównane do prawej (`>`) w polu o szerokości `w` znaków; brakujące miejsca są uzupełniane spacjami z lewej. Na przykład `f"{7:>3}"` daje `"  7"`, a `f"{123:>3}"` daje `"123"`.
* `len(str(x))` to liczba cyfr liczby naturalnej `x`, np. `len(str(144))` wynosi `3`.
* Spacje na początku wiersza są istotne. Nie dodawaj spacji na końcu wiersza.

"""


def tabliczka_mnozenia(n):
    szerokosc = len(str(n * n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j > 1:
                print(" ", end="")
            print(f"{i * j:>{szerokosc}}", end="")
        print()


if __name__ == "__main__":
    n = int(input())
    tabliczka_mnozenia(n)
