"""
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

* Najprościej użyć schematu Hornera.

"""


def wartosc_wielomianu_w_punkcie(wspolczynniki, x):
    """
    Funkcja zwraca wartosc wielomianu w punkcie x.
    """
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik += wspolczynniki[i] * x**i
    return wynik


def test_wartosc_wielomianu_w_punkcie():
    assert wartosc_wielomianu_w_punkcie([1, 2, 3, 4], 2) == 49
    assert wartosc_wielomianu_w_punkcie([1, 2, 3, 4], 3) == 142


if __name__ == "__main__":
    test_wartosc_wielomianu_w_punkcie()
