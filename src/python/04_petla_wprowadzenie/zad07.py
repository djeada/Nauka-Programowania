r"""
ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` i oblicz $\pi^n$, mnożąc w pętli liczbę $\pi$ przez siebie. Wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba — $\pi^n$ zaokrąglona do dwóch miejsc po przecinku.

### Ograniczenia

* `0 ≤ n ≤ 20`

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi

* $\pi^0 = 1$, więc dla `n = 0` wypisz `1.00`.

"""

from math import pi


def potega_pi(n):
    wynik = 1.0
    for _ in range(n):
        wynik *= pi
    return wynik


if __name__ == "__main__":
    n = int(input())
    print(f"{potega_pi(n):.2f}")
