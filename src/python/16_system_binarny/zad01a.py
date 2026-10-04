r"""
ZAD-01A — Dziesiętny → binarny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` zapisaną w systemie dziesiętnym i wypisz jej zapis w systemie binarnym.

### Wejście

* 1. linia: `n` — liczba naturalna

### Wyjście

Jedna linia: zapis binarny liczby `n`.

### Ograniczenia

* $0 \le n \le 10^9$

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
11
```

### Uwagi

* Dla `n = 0` wypisz `0`.
* Spróbuj obejść się bez wbudowanej funkcji `bin()`: kolejne cyfry binarne to reszty z dzielenia przez 2 (od najmniej znaczącej).

"""


def na_binarny(n):
    """Zwraca zapis binarny liczby naturalnej n (dla n = 0 jest to "0")."""
    if n == 0:
        return "0"
    zapis = ""
    while n > 0:
        zapis = str(n % 2) + zapis
        n //= 2
    return zapis


if __name__ == "__main__":
    n = int(input())
    print(na_binarny(n))
