r"""
ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` i za pomocą pętli oblicz trzy sumy:

a) $\sum_{k=1}^{n} (k^2 + k + 1)$

b) $\sum_{k=1}^{n} (k^2 + 5k)$

c) $\sum_{k=1}^{n} 3k$

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 1`)

### Wyjście

Trzy liczby całkowite, każda w osobnej linii: suma a), suma b) i suma c).

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
20
9
```

Dla `n = 2`: a) $3 + 7 = 10$, b) $6 + 14 = 20$, c) $3 + 6 = 9$.

"""


def suma_a(n):
    suma = 0
    for k in range(1, n + 1):
        suma += k**2 + k + 1
    return suma


def suma_b(n):
    suma = 0
    for k in range(1, n + 1):
        suma += k**2 + 5 * k
    return suma


def suma_c(n):
    suma = 0
    for k in range(1, n + 1):
        suma += 3 * k
    return suma


if __name__ == "__main__":
    n = int(input())

    print(suma_a(n))
    print(suma_b(n))
    print(suma_c(n))
