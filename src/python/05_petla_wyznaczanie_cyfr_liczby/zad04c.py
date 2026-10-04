r"""
ZAD-04C — Cyfry różne od zera

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `warunki`

### Treść

Wczytaj liczbę naturalną `n` i wypisz od końca wszystkie jej cyfry, które są **różne od zera**.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Niezerowe cyfry liczby `n` od końca, każda w osobnej linii.
Jeśli takich cyfr nie ma (czyli `n = 0`), nie wypisuj nic.

### Przykład

**Wejście:**

```
650
```

**Wyjście:**

```
5
6
```

Ostatnia cyfra `0` jest pomijana, potem wypisujemy `5` i `6`.

"""


def wypisz_niezerowe_cyfry(n):
    while n > 0:
        cyfra = n % 10
        if cyfra != 0:
            print(cyfra)
        n //= 10


if __name__ == "__main__":
    n = int(input())
    wypisz_niezerowe_cyfry(n)
