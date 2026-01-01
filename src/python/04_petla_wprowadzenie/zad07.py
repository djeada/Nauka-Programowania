"""
ZAD-07 — Potęgowanie liczby π

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `potęgi`, `formatowanie`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 0`), oblicz wartość ( \pi^n ) i wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba zmiennoprzecinkowa — ( \pi^n ) z dokładnością do dwóch miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
9.87
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz `1.00`.

"""

from math import pi

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    wynik = 1
    for i in range(liczba):
        wynik = wynik * pi

    print("Wynik: ", round(wynik, 2))
