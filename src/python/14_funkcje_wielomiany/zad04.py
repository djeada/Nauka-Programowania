"""
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` i zwraca listę współczynników wielomianu będącego ich iloczynem.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)

### Przykład

Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
`[5, 10, 30, 26, 52, 24]`

"""


def iloczyn_wielomianow(wielomian_a, wielomian_b):
    """
    Funkcja zwraca wspolczynniki wielomianu bedacego iloczynem wielomianow a i b.
    
    Złożoność czasowa: O(n * m), gdzie n i m to długości wielomianów
    Złożoność pamięciowa: O(n + m) dla wyniku
    """

    wynik = [0 for i in range(len(wielomian_a) + len(wielomian_b) - 1)]

    for i in range(len(wielomian_a)):
        for j in range(len(wielomian_b)):
            wynik[i + j] += wielomian_a[i] * wielomian_b[j]

    return wynik


def test_iloczyn_wielomianow():
    assert iloczyn_wielomianow([1, 1, 0], [-5, 0, 0, 2]) == [-5, -5, 0, 2, 2, 0]


if __name__ == "__main__":
    # Wczytanie dwóch wielomianów jako listy
    wielomian_a = __import__("ast").literal_eval(input().strip())
    wielomian_b = __import__("ast").literal_eval(input().strip())
    
    # Iloczyn wielomianów
    # Złożoność czasowa: O(n * m)
    # Złożoność pamięciowa: O(n + m)
    wynik = iloczyn_wielomianow(wielomian_a, wielomian_b)
    
    # Wypisanie wyniku jako lista
    print(str(wynik))
