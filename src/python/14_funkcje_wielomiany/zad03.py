r"""
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję `suma_wielomianow(a, b)`, która otrzymuje listy współczynników dwóch wielomianów (mogą mieć różne stopnie) i zwraca listę współczynników ich sumy.

Program wczytuje oba wielomiany, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb całkowitych `b_m ... b_0`

### Wyjście

Jedna linia: dokładnie `max(n, m) + 1` liczb całkowitych — współczynniki sumy od najwyższej potęgi, oddzielone spacją. Nie usuwaj zer z początku wyniku (np. gdy najwyższe potęgi się zredukują).

### Ograniczenia

* `0 ≤ n, m ≤ 10`
* `-100 ≤ a_i, b_i ≤ 100`

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

$(3x^2 + 5x + 2) + (2x^2 - 8x + 1) = 5x^2 - 3x + 3$.

### Uwagi

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej listy. Np. `1 2 3 4` + `5 6` = `1 2 8 10`.

### Kod startowy

```python
def suma_wielomianow(a, b):
    pass


n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]
print(*suma_wielomianow(a, b))
```

"""


def suma_wielomianow(a, b):
    """Zwraca współczynniki sumy dwóch wielomianów (od najwyższej potęgi)."""
    dlugosc = max(len(a), len(b))
    # Wyrównanie „od końca”: zera dopisujemy na początku krótszej listy.
    a = [0] * (dlugosc - len(a)) + a
    b = [0] * (dlugosc - len(b)) + b
    return [x + y for x, y in zip(a, b)]


if __name__ == "__main__":
    n = int(input())
    a = [int(s) for s in input().split()]
    m = int(input())
    b = [int(s) for s in input().split()]
    print(*suma_wielomianow(a, b))
