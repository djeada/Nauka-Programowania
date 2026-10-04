r"""
ZAD-01 — Liczenie cyfr w liczbie

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz, z ilu cyfr składa się jej zapis dziesiętny.

### Wejście

* 1. linia: `n` — liczba naturalna (`n ≥ 0`)

### Wyjście

Jedna liczba całkowita — liczba cyfr liczby `n`.

### Przykład

**Wejście:**

```
342
```

**Wyjście:**

```
3
```

### Uwagi

* Dla `n = 0` poprawna odpowiedź to `1`.
* Licz cyfry w pętli, dzieląc liczbę przez `10`.

"""


def liczba_cyfr(n):
    licznik = 1
    n //= 10
    while n > 0:
        licznik += 1
        n //= 10
    return licznik


if __name__ == "__main__":
    n = int(input())
    print(liczba_cyfr(n))
