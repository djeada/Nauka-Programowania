r"""
ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile bitów równych `1` ma jej zapis binarny.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

### Uwagi

* Najmłodszy bit to `n & 1`, a `n >> 1` usuwa go z liczby. Dla `n = 0` wynik to `0`.

"""


def liczba_jedynek(n):
    """Zwraca liczbę bitów równych 1 w zapisie binarnym n."""
    jedynki = 0
    while n > 0:
        jedynki += n & 1
        n >>= 1
    return jedynki


if __name__ == "__main__":
    n = int(input())
    print(liczba_jedynek(n))
