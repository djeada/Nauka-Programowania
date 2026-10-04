r"""
ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz jej cyfry od końca — zaczynając od cyfry jedności, a kończąc na najwyższej cyfrze.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Cyfry liczby `n` od końca, każda w osobnej linii.

### Przykład

**Wejście:**

```
8214
```

**Wyjście:**

```
4
1
2
8
```

### Uwagi

* Dla `n = 0` wypisz jedną linię: `0`.
* Zera w środku i na końcu liczby też są cyframi — np. dla `120` wypisz `0`, `2`, `1`.

"""


def wypisz_cyfry_od_konca(n):
    print(n % 10)
    n //= 10
    while n > 0:
        print(n % 10)
        n //= 10


if __name__ == "__main__":
    n = int(input())
    wypisz_cyfry_od_konca(n)
