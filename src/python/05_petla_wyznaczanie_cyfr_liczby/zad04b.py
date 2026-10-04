r"""
ZAD-04B — Cyfry mniejsze niż 5

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz od końca wszystkie jej cyfry, które są **mniejsze niż 5**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Cyfry liczby `n` mniejsze niż `5`, od końca, każda w osobnej linii.
Jeśli takich cyfr nie ma, nie wypisuj nic.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
1
0
1
```

### Uwagi

* Cyfra `5` nie jest mniejsza niż `5`.
* Dla `n = 0` wypisz `0`.

"""


def wypisz_cyfry_mniejsze_niz_5(n):
    while True:
        cyfra = n % 10
        if cyfra < 5:
            print(cyfra)
        n //= 10
        if n == 0:
            break


if __name__ == "__main__":
    n = int(input())
    wypisz_cyfry_mniejsze_niz_5(n)
