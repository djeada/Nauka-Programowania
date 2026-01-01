"""
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `pochodna`, `wielomiany`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

* Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
* Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.

### Przykład

**Wejście:**

```
2
4 -3 2
1
```

**Wyjście:**

```
8 -3
```

### Uwagi o formatowaniu

* Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:
  `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]`.

"""


def wyraz_ciag_fibonacciego(n):
    """
    Funkcja oblicza n-ty wyraz ciagu Fibonacciego.
    """
    if n < 0:
        raise ValueError("Liczba musi byc nieujemna")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return wyraz_ciag_fibonacciego(n - 1) + wyraz_ciag_fibonacciego(n - 2)


def test_wyraz_ciag_fibonacciego():
    assert wyraz_ciag_fibonacciego(0) == 0
    assert wyraz_ciag_fibonacciego(1) == 1
    assert wyraz_ciag_fibonacciego(12) == 144


if __name__ == "__main__":

    test_wyraz_ciag_fibonacciego()
