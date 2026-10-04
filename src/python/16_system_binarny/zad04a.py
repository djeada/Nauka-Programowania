r"""
ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile cyfr `0` ma jej zapis binarny (bez zer wiodących).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Zapis binarny `0` to `0`, więc dla `n = 0` wynik to `1`.

"""


def liczba_zer(n):
    """Zwraca liczbę zer w zapisie binarnym n (bez zer wiodących; dla n = 0 wynik to 1)."""
    if n == 0:
        return 1
    zera = 0
    while n > 0:
        if n & 1 == 0:
            zera += 1
        n >>= 1
    return zera


if __name__ == "__main__":
    n = int(input())
    print(liczba_zer(n))
