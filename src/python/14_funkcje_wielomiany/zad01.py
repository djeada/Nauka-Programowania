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
    Współczynniki w formacie [a_n, ..., a_0] (najwyższy stopień pierwszy).

    Złożoność czasowa: O(n), gdzie n to stopień wielomianu
    Złożoność pamięciowa: O(1)
    """
    wynik = 0
    n = len(wspolczynniki)
    for i in range(n):
        # wspolczynniki[i] to współczynnik przy x^(n-1-i)
        wynik += wspolczynniki[i] * (x ** (n - 1 - i))
    return wynik


def test_wartosc_wielomianu_w_punkcie():
    assert wartosc_wielomianu_w_punkcie([1, 2, 3, 4], 2) == 49
    assert wartosc_wielomianu_w_punkcie([1, 2, 3, 4], 3) == 142


if __name__ == "__main__":
    # Wczytanie współczynników wielomianu jako listy
    wspolczynniki = __import__("ast").literal_eval(input().strip())
    # Wczytanie punktu x
    x = int(input().strip())

    # Obliczenie wartości wielomianu
    # Złożoność czasowa: O(n)
    # Złożoność pamięciowa: O(1)
    wynik = wartosc_wielomianu_w_punkcie(wspolczynniki, x)

    # Wypisanie wyniku
    print(wynik)
