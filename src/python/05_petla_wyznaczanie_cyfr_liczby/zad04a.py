r"""
ZAD-04A — Cyfry parzyste

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz od końca wszystkie jej cyfry, które są **parzyste**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Parzyste cyfry liczby `n` od końca, każda w osobnej linii.
Jeśli `n` nie ma parzystych cyfr, nie wypisuj nic.

### Przykład

**Wejście:**

```
932
```

**Wyjście:**

```
2
```

### Uwagi

* `0` jest cyfrą parzystą, więc dla `n = 0` wypisz `0`.
* Każde wystąpienie cyfry wypisz osobno — np. dla `4004` wypisz `4`, `0`, `0`, `4`.

"""


def wypisz_parzyste_cyfry(n):
    while True:
        cyfra = n % 10
        if cyfra % 2 == 0:
            print(cyfra)
        n //= 10
        if n == 0:
            break


if __name__ == "__main__":
    n = int(input())
    wypisz_parzyste_cyfry(n)
