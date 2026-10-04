r"""
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję `iloczyn_wielomianow(a, b)`, która otrzymuje listy współczynników dwóch wielomianów i zwraca listę współczynników ich iloczynu.

Program wczytuje oba wielomiany, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb całkowitych `b_m ... b_0`

### Wyjście

Jedna linia: dokładnie `n + m + 1` liczb całkowitych — współczynniki iloczynu od najwyższej potęgi, oddzielone spacją.

### Ograniczenia

* `0 ≤ n, m ≤ 10`
* `-100 ≤ a_i, b_i ≤ 100`

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

$(5x^3 + 10x + 6)(x^2 + 2x + 4) = 5x^5 + 10x^4 + 30x^3 + 26x^2 + 52x + 24$.

### Uwagi

* Każdy wyraz pierwszego wielomianu mnożymy przez każdy wyraz drugiego: $a_i x^i \cdot b_j x^j = a_i b_j x^{i+j}$. Utwórz listę `n + m + 1` zer i dla każdej pary pozycji `i` (w liście `a`) oraz `j` (w liście `b`) dodaj `a[i] * b[j]` do pozycji `i + j` wyniku.

### Kod startowy

```python
def iloczyn_wielomianow(a, b):
    pass


n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]
print(*iloczyn_wielomianow(a, b))
```

"""


def iloczyn_wielomianow(a, b):
    """Zwraca współczynniki iloczynu dwóch wielomianów (od najwyższej potęgi)."""
    wynik = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            wynik[i + j] += a[i] * b[j]
    return wynik


if __name__ == "__main__":
    n = int(input())
    a = [int(s) for s in input().split()]
    m = int(input())
    b = [int(s) for s in input().split()]
    print(*iloczyn_wielomianow(a, b))
