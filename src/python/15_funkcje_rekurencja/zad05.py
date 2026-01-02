"""
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `wielomiany`, `pochodna`, `rekurencja`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

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
        print(' '.join(map(str, wynik)))
