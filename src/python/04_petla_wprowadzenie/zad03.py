r"""
ZAD-03 — Wypisywanie liczby π z rosnącą dokładnością

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` i wypisz liczbę $\pi$ w `n` liniach: w pierwszej z dokładnością do `1` miejsca po przecinku, w drugiej do `2` miejsc, …, w `n`-tej do `n` miejsc po przecinku.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

`n` linii; w `k`-tej linii liczba $\pi$ zaokrąglona do `k` miejsc po przecinku.

### Ograniczenia

* `1 ≤ n ≤ 15`

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
3.1
3.14
3.142
```

### Uwagi

* Wartość $\pi$ weź z modułu `math` (`math.pi`).
* Liczbę miejsc po przecinku możesz podać w f-stringu jako zmienną: `f"{math.pi:.{k}f}"` wypisze $\pi$ z dokładnością do `k` miejsc.
* Stosuj standardowe zaokrąglanie, np. przy `4` miejscach wypisz `3.1416`.
* Liczby zmiennoprzecinkowe mają ograniczoną precyzję — `math.pi` jest dokładne mniej więcej do 15. miejsca po przecinku, dlatego `n ≤ 15`.

"""

from math import pi


def wypisz_pi(n):
    for k in range(1, n + 1):
        print(f"{pi:.{k}f}")


if __name__ == "__main__":
    n = int(input())
    wypisz_pi(n)
