r"""
ZAD-06 — Maksimum z czterech liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `if`, `porównania`

### Treść

Wczytaj cztery liczby naturalne i wypisz największą z nich.

### Wejście

4 linie: `a`, `b`, `c`, `d` — liczby całkowite z zakresu $0 \dots 10^9$.

### Wyjście

Jedna linia: największa z czterech liczb.

### Przykład

**Wejście:**

```
2
5
1
4
```

**Wyjście:**

```
5
```

### Uwagi

* Spróbuj rozwiązać zadanie instrukcją `if`, bez wbudowanej funkcji `max`.

"""


def wieksza(x, y):
    if x > y:
        return x
    else:
        return y


def maksimum_z_czterech(a, b, c, d):
    return wieksza(wieksza(a, b), wieksza(c, d))


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(maksimum_z_czterech(a, b, c, d))
