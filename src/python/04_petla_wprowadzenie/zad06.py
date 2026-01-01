"""
ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

"""

if __name__ == "__main__":

    print("Podaj liczbe n: ")
    n = int(input())

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = n/(n + 1) wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += i / (i + 1)

    print(suma)

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = (n^2 + 5)/n wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += (i**2 + 5) / i

    print(suma)

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = n + 2^n wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += i + 2**i

    print(suma)
