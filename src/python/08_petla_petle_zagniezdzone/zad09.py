r"""
ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `pierwszość`

### Treść

Wczytaj liczbę naturalną `N` i wypisz `N` pierwszych liczb pierwszych w jednej linii, w kolejności rosnącej.

### Wejście

* 1. linia: `N` — liczba naturalna (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych pojedynczą spacją.

### Ograniczenia

* `1 ≤ N ≤ 1000`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi

* Pętla zewnętrzna sprawdza kolejne liczby, a wewnętrzna szuka ich dzielników. Wystarczy sprawdzać dzielniki `d` spełniające $d \cdot d \leq x$.

"""


def czy_pierwsza(x):
    if x < 2:
        return False
    dzielnik = 2
    while dzielnik * dzielnik <= x:
        if x % dzielnik == 0:
            return False
        dzielnik += 1
    return True


def wypisz_liczby_pierwsze(n):
    znalezione = 0
    kandydat = 2
    while znalezione < n:
        if czy_pierwsza(kandydat):
            if znalezione > 0:
                print(" ", end="")
            print(kandydat, end="")
            znalezione += 1
        kandydat += 1
    print()


if __name__ == "__main__":
    n = int(input())
    wypisz_liczby_pierwsze(n)
