r"""
ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `kombinatoryka`

### Treść

Wczytaj liczbę naturalną `n` i wypisz `n` pierwszych wierszy trójkąta Pascala.

Każdy wiersz zaczyna się i kończy liczbą `1`, a każda liczba w środku wiersza jest sumą dwóch liczb stojących nad nią w poprzednim wierszu:

```
1
1 1
1 2 1
1 3 3 1
```

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii; w `i`-tej linii jest `i` liczb oddzielonych pojedynczą spacją.

### Ograniczenia

* `1 ≤ n ≤ 30`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi

* Liczby w wierszu numer $r$ (licząc od $0$) to symbole Newtona $\binom{r}{0}, \binom{r}{1}, \ldots, \binom{r}{r}$. Kolejną liczbę w wierszu można obliczyć z poprzedniej: $\binom{r}{k+1} = \binom{r}{k} \cdot \frac{r - k}{k + 1}$ — wtedy nie potrzebujesz zapamiętywać poprzedniego wiersza.

"""


def trojkat_pascala(n):
    for r in range(n):
        wartosc = 1
        for k in range(r + 1):
            if k > 0:
                print(" ", end="")
            print(wartosc, end="")
            wartosc = wartosc * (r - k) // (k + 1)
        print()


if __name__ == "__main__":
    n = int(input())
    trojkat_pascala(n)
