"""
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `listy`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` (mogą mieć różne stopnie) i zwraca współczynniki wielomianu będącego ich sumą.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników `a + b` w tej samej konwencji

### Przykład

Dla `a = [3, 5, 2]` i `b = [2, -8, 1]` funkcja zwraca:
`[5, -3, 3]`

### Uwagi

* Jeśli listy mają różne długości, wyrównaj je od końca (od wyrazu wolnego).

"""


def suma_wielomianow(wielomian_a, wielomian_b):
    """
    Funkcja sumuje dwie listy wielomianow.
    """
    min_dlugosc = min(len(wielomian_a), len(wielomian_b))

    wynik = [wielomian_a[i] + wielomian_b[i] for i in range(min_dlugosc)]

    for i in range(min_dlugosc, len(wielomian_a)):
        wynik.append(wielomian_a[i])

    for i in range(min_dlugosc, len(wielomian_b)):
        wynik.append(wielomian_b[i])

    return wynik


def test_suma_wielomianow():
    assert suma_wielomianow([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
    assert suma_wielomianow([1, 2, 3], [1, 2, 3, 4]) == [2, 4, 6, 4]


if __name__ == "__main__":
    test_suma_wielomianow()
