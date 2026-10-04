r"""
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję `pochodna(wspolczynniki, k)`, która zwraca listę współczynników wielomianu będącego `k`-tą pochodną danego wielomianu (czyli wielomianu zróżniczkowanego `k` razy).

Program wczytuje wielomian i liczbę `k`, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

Jedna linia: współczynniki `k`-tej pochodnej od najwyższej potęgi, oddzielone spacją. Jeśli `k > n`, pochodna jest wielomianem zerowym — wypisz wtedy `0`.

### Ograniczenia

* `0 ≤ n ≤ 10`, `1 ≤ k ≤ 12`
* `-100 ≤ a_i ≤ 100`

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

$(4x^2 - 3x + 2)' = 8x - 3$.

### Uwagi

* Pochodna jednomianu: $(a x^d)' = d \cdot a x^{d-1}$, a pochodna stałej to $0$. Jeśli współczynniki to `[c_d, c_{d-1}, ..., c_1, c_0]`, to pierwsza pochodna ma współczynniki `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]` (o jeden mniej).
* `k`-tą pochodną otrzymasz, licząc pierwszą pochodną `k` razy.

### Kod startowy

```python
def pochodna(wspolczynniki, k):
    pass


n = int(input())
wspolczynniki = [int(s) for s in input().split()]
k = int(input())
print(*pochodna(wspolczynniki, k))
```

"""


def pierwsza_pochodna(wspolczynniki):
    """Zwraca współczynniki pierwszej pochodnej wielomianu."""
    stopien = len(wspolczynniki) - 1
    if stopien == 0:
        return [0]
    return [wspolczynniki[i] * (stopien - i) for i in range(stopien)]


def pochodna(wspolczynniki, k):
    """Zwraca współczynniki k-tej pochodnej wielomianu ([0] dla wielomianu zerowego)."""
    wynik = wspolczynniki
    for _ in range(k):
        wynik = pierwsza_pochodna(wynik)
    return wynik


if __name__ == "__main__":
    n = int(input())
    wspolczynniki = [int(s) for s in input().split()]
    k = int(input())
    print(*pochodna(wspolczynniki, k))
