r"""
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję `pomnoz_przez_skalar(wspolczynniki, k)`, która zwraca **nową** listę współczynników wielomianu $k \cdot W(x)$, czyli wielomianu powstałego przez pomnożenie każdego współczynnika przez liczbę $k$.

Program wczytuje wielomian i liczbę $k$, wywołuje funkcję i wypisuje współczynniki wyniku.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych `a_n ... a_0`
* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych — współczynniki po pomnożeniu, oddzielone spacją. Liczba współczynników się nie zmienia (także dla `k = 0`).

### Ograniczenia

* `0 ≤ n ≤ 10`
* `-100 ≤ a_i ≤ 100`, `-100 ≤ k ≤ 100`

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

### Kod startowy

```python
def pomnoz_przez_skalar(wspolczynniki, k):
    pass


n = int(input())
wspolczynniki = [int(s) for s in input().split()]
k = int(input())
print(*pomnoz_przez_skalar(wspolczynniki, k))
```

"""


def pomnoz_przez_skalar(wspolczynniki, k):
    """Zwraca nową listę współczynników wielomianu pomnożonego przez k."""
    return [a * k for a in wspolczynniki]


if __name__ == "__main__":
    n = int(input())
    wspolczynniki = [int(s) for s in input().split()]
    k = int(input())
    print(*pomnoz_przez_skalar(wspolczynniki, k))
