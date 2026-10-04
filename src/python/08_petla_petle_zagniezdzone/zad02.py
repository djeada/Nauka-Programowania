r"""
ZAD-02 — Trójkąt prostokątny (rosnący)

**Poziom:** ★☆☆
**Tagi:** `pętle zagnieżdżone`, `print`, `string`

### Treść

Wczytaj liczbę naturalną `n` i wypisz trójkąt o wysokości `n`: w wierszu numer `i` (licząc od `1`) ma być `i` gwiazdek.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii: w pierwszej `1` gwiazdka, w drugiej `2` gwiazdki, …, w ostatniej `n` gwiazdek.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
**
***
```

"""


def trojkat_rosnacy(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print("*", end="")
        print()


if __name__ == "__main__":
    n = int(input())
    trojkat_rosnacy(n)
