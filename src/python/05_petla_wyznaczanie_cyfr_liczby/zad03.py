r"""
ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n`, oblicz sumę jej cyfr i wypisz wynik.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba całkowita — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

$1 + 2 + 9 = 12$.

### Uwagi

* Dla `n = 0` suma cyfr wynosi `0`.

"""


def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma


if __name__ == "__main__":
    n = int(input())
    print(suma_cyfr(n))
