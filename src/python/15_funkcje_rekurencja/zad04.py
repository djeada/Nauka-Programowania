"""
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `wielomiany`, `konwolucja`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich iloczynem.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki iloczynu (długość `n+m+1`), oddzielone spacją.

### Przykład

**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

**Wyjście:**

```
5 10 30 26 52 24
```

"""


def silnia(n):
    """
    Funkcja oblicza silnie z n.
    """
    if n < 0:
        raise ValueError("Silnia jest niezdefiniowana dla liczb ujemnych.")

    if n <= 1:
        return 1

    return n * silnia(n - 1)


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(5) == 120
    assert silnia(10) == 3628800


if __name__ == "__main__":
    test_silnia()
