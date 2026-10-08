r"""
ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `maski`, `bez if`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `abs`, `min`, `max`, `sorted`.

### Wejście

* 1. linia: `x`

### Wyjście

Jedna liczba naturalna: $|x|$.

### Ograniczenia

* $-10^9 \le x \le 10^9$ — liczba **może być ujemna**

### Przykład

**Wejście:**

```
-12
```

**Wyjście:**

```
12
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są potrzebne.
* Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
* XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity, czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch). Wystarczy więc obliczyć `(x ^ m) - m`.

"""


def wartosc_bezwzgledna(x):
    """
    Zwraca |x| bez instrukcji warunkowych.
    Maska znaku m = x >> 63 to -1 dla x < 0 i 0 dla x >= 0;
    (x ^ m) - m daje x dla m = 0 oraz (-x - 1) + 1 = -x dla m = -1.
    """
    maska = x >> 63
    return (x ^ maska) - maska


if __name__ == "__main__":
    x = int(input())
    print(wartosc_bezwzgledna(x))
