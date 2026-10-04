r"""
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `min`, `max`, `abs`, `sorted`.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna wartość).

### Ograniczenia

* $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.
* Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)` jest równe `d` albo `0`.
* Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.

"""


def minimum(a, b):
    """
    Zwraca mniejszą z liczb bez instrukcji warunkowych.
    Przesunięcie w prawo liczby ujemnej daje -1 (same jedynki), a nieujemnej 0,
    więc maska to -1, gdy a < b, i 0 w przeciwnym razie.
    """
    roznica = a - b
    maska = roznica >> 63
    return b + (roznica & maska)


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(minimum(a, b))
