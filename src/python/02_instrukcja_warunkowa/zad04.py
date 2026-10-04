r"""
ZAD-04 — Maksimum i minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **najpierw większa, potem mniejsza**, oddzielone pojedynczą spacją.
Jeśli $a = b$, wypisz tę samą liczbę dwa razy.

### Wejście

* 1 linia: `a` — liczba całkowita, $0 \le a \le 10^9$
* 2 linia: `b` — liczba całkowita, $0 \le b \le 10^9$

### Wyjście

Jedna linia: większa liczba, spacja, mniejsza liczba.

### Przykład 1

**Wejście:**

```
1
4
```

**Wyjście:**

```
4 1
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
5 5
```

### Uwagi

* Spróbuj rozwiązać zadanie instrukcją `if`, bez wbudowanych funkcji `max` i `min`.

"""


def wieksza_i_mniejsza(a, b):
    if a >= b:
        return f"{a} {b}"
    else:
        return f"{b} {a}"


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(wieksza_i_mniejsza(a, b))
