r"""
ZAD-07 — Choinka z N trójkątów

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `generowanie`, `print`

### Treść

Wczytaj liczbę naturalną `N` i wypisz choinkę złożoną z `N` trójkątów ustawionych jeden pod drugim. Pierwszy trójkąt ma wysokość `1`, drugi `2`, …, ostatni `N`.

Każdy trójkąt jest rosnący (jak w ZAD-02): w jego `i`-tym wierszu jest `i` gwiazdek.

### Wejście

* 1. linia: `N` — liczba naturalna (`N ≥ 1`)

### Wyjście

$1 + 2 + \ldots + N$ linii — kolejne trójkąty, bez pustych linii między nimi.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
*
**
*
**
***
```

"""


def trojkat(wysokosc):
    for i in range(1, wysokosc + 1):
        for _ in range(i):
            print("*", end="")
        print()


def choinka(n):
    for wysokosc in range(1, n + 1):
        trojkat(wysokosc)


if __name__ == "__main__":
    n = int(input())
    choinka(n)
