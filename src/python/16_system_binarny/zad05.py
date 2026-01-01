"""
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `min(a, b)`.

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

ZAD-05B — Maksimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `max(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
3
```

"""


def znak(n):
    """
    Funkcja zwraca znak liczby n.
    """
    return (n >> 31) & 0x01


def maksimum(a, b):
    """
    Funkcja zwraca maksimum dwoch liczb.
    dla a >= b: znak_a = 1, znak_b = 0;
    dla a < b: znak_a = 0, znak_b = 1;
    """
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_a * a + znak_b * b


def minimum(a, b):
    """
    Funkcja zwraca minimum dwoch liczb.
    dla a >= b: znak_a = 0, znak_b = 1;
    dla a < b: znak_a = 1, znak_b = 0;
    """
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_b * a + znak_a * b


def test_maksimum():
    assert maksimum(2, 3) == 3
    assert maksimum(3, 2) == 3
    assert maksimum(3, 3) == 3
    assert maksimum(0, 0) == 0
    assert maksimum(-2, -3) == -2
    assert maksimum(-3, -2) == -2
    assert maksimum(-3, -3) == -3


def test_minimum():
    assert minimum(2, 3) == 2
    assert minimum(3, 2) == 2
    assert minimum(3, 3) == 3
    assert minimum(0, 0) == 0
    assert minimum(-2, -3) == -3
    assert minimum(-3, -2) == -3
    assert minimum(-3, -3) == -3


if __name__ == "__main__":

    test_minimum()
    test_maksimum()
