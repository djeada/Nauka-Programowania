r"""
ZAD-04 — Sumowanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `sumowanie`, `pętle`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `n` i za pomocą pętli oblicz sumę wszystkich liczb naturalnych dodatnich mniejszych od `n`, czyli $1 + 2 + \ldots + (n - 1)$.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Jedna liczba całkowita — suma liczb od `1` do `n - 1`.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
10
```

$1 + 2 + 3 + 4 = 10$.

### Uwagi

* Dla `n = 1` suma jest pusta, więc wynik to `0`.

"""


def suma_mniejszych(n):
    suma = 0
    for liczba in range(1, n):
        suma += liczba
    return suma


if __name__ == "__main__":
    n = int(input())
    print(suma_mniejszych(n))
