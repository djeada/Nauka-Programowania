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
    
    Złożoność czasowa: O(k * n), gdzie n to stopień wielomianu
    Złożoność pamięciowa: O(n) dla wyniku
    """
    if not wielomian or k < 0:
        return [0]
    
    wynik = wielomian[:]
    
    for _ in range(k):
        if len(wynik) <= 1:
            wynik = [0]
            break
        
        nowy_wynik = []
        n = len(wynik)
        for i in range(n - 1):
            nowy_wynik.append(wynik[i] * (n - i - 1))
        wynik = nowy_wynik
    
    return wynik if wynik else [0]


def test_pochodna():
    assert pochodna([4, -3, 2], 1) == [8, -3]
    assert pochodna([13, -6, 0, -1, -1], 2) == [156, -36, 0]


if __name__ == "__main__":
    # Wczytanie wielomianu jako listy
    wielomian = eval(input().strip())
    # Wczytanie stopnia pochodnej
    k = int(input().strip())
    
    # Obliczenie k-tej pochodnej
    # Złożoność czasowa: O(k * n)
    # Złożoność pamięciowa: O(n)
    wynik = pochodna(wielomian, k)
    
    # Wypisanie wyniku jako lista
    print(str(wynik))
