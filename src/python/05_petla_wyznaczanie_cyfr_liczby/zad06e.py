r"""
ZAD-06E — Mniejsze od n złożone wyłącznie z parzystych cyfr

**Poziom:** ★★☆
**Tagi:** `pętle`, `warunki`, `cyfry`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz w kolejności rosnącej wszystkie liczby naturalne `x` takie, że `1 ≤ x < n` i **każda** cyfra liczby `x` jest parzysta.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Liczby spełniające warunek, każda w osobnej linii.
Jeśli takich liczb nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
50
```

**Wyjście:**

```
2
4
6
8
20
22
24
26
28
40
42
44
46
48
```

### Uwagi

* `0` jest cyfrą parzystą, więc np. `20` i `40` spełniają warunek.
* Samą liczbę `0` pomijamy (zaczynamy od `x = 1`).

"""


def same_parzyste_cyfry(liczba):
    while liczba > 0:
        if liczba % 10 % 2 != 0:
            return False
        liczba //= 10
    return True


if __name__ == "__main__":
    n = int(input())

    for x in range(1, n):
        if same_parzyste_cyfry(x):
            print(x)
