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


def pochodna_rek(wspolczynniki, k):
    """
    Oblicza k-tą pochodną wielomianu rekurencyjnie.

    Złożoność czasowa: O(k * n)
    Złożoność pamięciowa: O(k * n)
    """
    if k == 0:
        return wspolczynniki
    if not wspolczynniki or len(wspolczynniki) == 1:
        return []

    # Pierwsza pochodna
    n = len(wspolczynniki)
    pochodna1 = []
    for i in range(n - 1):
        pochodna1.append(wspolczynniki[i] * (n - 1 - i))

    # Rekurencyjnie dla k-1
    return pochodna_rek(pochodna1, k - 1)


if __name__ == "__main__":
    n = int(input().strip())
    wspolczynniki = list(map(int, input().strip().split()))
    k = int(input().strip())
    wynik = pochodna_rek(wspolczynniki, k)
    if not wynik:
        print("[]")
    else:
        print(" ".join(map(str, wynik)))
