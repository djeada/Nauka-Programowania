"""
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

"""


def potega(a, b):
    """
    Funkcja oblicza a podniesione do b.
    """

    if b < 0:
        return 1 / potega(a, -b)

    if b == 0:
        return 1
    else:
        return a * potega(a, b - 1)


def test_potega():
    assert potega(2, 3) == 8
    assert potega(2, 0) == 1
    assert potega(2, -3) == 0.125


if __name__ == "__main__":
    test_potega()
