r"""
ZAD-03 — Trójkąt prostokątny (malejący)

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` i wypisz odwrócony trójkąt o wysokości `n`: w pierwszym wierszu `n` gwiazdek, w każdym kolejnym o jedną mniej.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii: w pierwszej `n` gwiazdek, w drugiej `n - 1`, …, w ostatniej `1` gwiazdka.

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
****
***
**
*
```

"""


def trojkat_malejacy(n):
    for i in range(n, 0, -1):
        for _ in range(i):
            print("*", end="")
        print()


if __name__ == "__main__":
    n = int(input())
    trojkat_malejacy(n)
