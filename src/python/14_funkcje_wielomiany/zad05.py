"""
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `k` — liczba naturalna

### Wyjście (zwracana wartość)

* lista współczynników wielomianu po zróżniczkowaniu `k` razy

### Przykład

Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
`[8, -3]`

### Uwagi

* Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

"""


def pochodna(wielomian, k):
    """
    Funkcja oblicza k-ta pochodna wielomianu.
    """
    wynik = []
    kopia = wielomian[:]

    for i in range(k):
        wynik = []
        n = len(kopia)
        for i in range(n - 1):
            wynik.append(kopia[i] * (n - i - 1))
        kopia = wynik[:]

    return wynik


def test_pochodna():
    assert pochodna([4, -3, 2], 1) == [8, -3]
    assert pochodna([13, -6, 0, -1, -1], 2) == [156, -36, 0]


if __name__ == "__main__":

    test_pochodna()
