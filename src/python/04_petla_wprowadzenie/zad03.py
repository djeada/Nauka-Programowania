"""
ZAD-03 — Wypisywanie liczby π z określoną dokładnością

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

1. Wczytaj liczbę naturalną `n` (`n > 0`).
2. Wypisz liczbę π dokładnie `n` razy.
3. Każda wypisana wartość ma mieć **dokładnie `n` miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

`n` wierszy, w każdym liczba π z dokładnością do `n` miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
3.14
3.14
```

### Uwagi o formatowaniu

* Liczba miejsc po przecinku ma być **dokładnie** równa `n` (np. dla `n=1` wypisz `3.1`).
* Stosuj standardowe zaokrąglanie przy formatowaniu.

"""

from math import pi

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    print(f"Liczba Pi {liczba} razy: ")

    for i in range(liczba):
        print(f"{i+1}. {pi:.{liczba}f}")
