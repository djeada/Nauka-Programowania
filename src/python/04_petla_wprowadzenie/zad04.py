"""
ZAD-04 — Sumowanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `sumowanie`, `pętle`, `arytmetyka`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`). Oblicz sumę wszystkich liczb naturalnych mniejszych od `n`, czyli:
`1 + 2 + ... + (n - 1)`
Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Jedna liczba naturalna — suma liczb od `1` do `n - 1`.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
10
```

### Uwagi o formatowaniu

* Dla `n = 1` wynik to `0`.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    suma = 0
    for i in range(1, liczba):
        suma += i

    print("Suma wszystkich liczb mniejszych od podanej liczby wynosi: ", suma)
