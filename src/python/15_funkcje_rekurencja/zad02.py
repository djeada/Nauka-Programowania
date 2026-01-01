"""
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `listy`, `I/O`

### Treść

Wczytaj współczynniki wielomianu oraz liczbę `k`. Wypisz współczynniki wielomianu powstałego przez pomnożenie każdego współczynnika przez `k`.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych (współczynniki po mnożeniu), oddzielonych spacją.

### Przykład

**Wejście:**

```
2
4 -3 2
-2
```

**Wyjście:**

```
-8 6 -4
```

"""


def suma_liczb_mniejszych_niz_n(n):
    """
    Funkcja oblicza sume liczb mniejszych od podanej liczby n.
    """

    if n < 1:
        return 0

    if n == 1:
        return 1

    return n + suma_liczb_mniejszych_niz_n(n - 1)


def test_suma_liczb_mniejszych_niz_n():

    assert suma_liczb_mniejszych_niz_n(1) == 1


if __name__ == "__main__":

    test_suma_liczb_mniejszych_niz_n()
