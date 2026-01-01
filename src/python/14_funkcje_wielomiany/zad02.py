"""
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `k` — liczba (całkowita)

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `k * P(x)`

### Przykład

Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
`[-8, 6, -4]`

"""


def mnozenie_wielomianu(wspolczynniki, x):
    """
    Funkcja zwraca wielomian bedacy wynikiem mnozenia otrzymanego wielomianu przez liczbe x.
    """
    return [wspolczynnik * x for wspolczynnik in wspolczynniki]


def test_mnozenie_wielomianu():
    assert mnozenie_wielomianu([1, 2, 3, 4], 2) == [2, 4, 6, 8]


if __name__ == "__main__":

    test_mnozenie_wielomianu()
