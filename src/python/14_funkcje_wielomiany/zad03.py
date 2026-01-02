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
    Współczynniki w formacie [a_n, ..., a_0] (najwyższy stopień pierwszy).
    
    Złożoność czasowa: O(max(n, m)), gdzie n i m to długości wielomianów
    Złożoność pamięciowa: O(max(n, m)) dla wyniku
    """
    # Wyrównanie długości od końca (od wyrazu wolnego)
    len_a = len(wielomian_a)
    len_b = len(wielomian_b)
    max_len = max(len_a, len_b)
    
    # Stworzenie wynikowej listy
    wynik = []
    
    # Dodawanie od końca (wyrazy wolne)
    for i in range(max_len):
        # Indeks od końca
        idx_a = len_a - 1 - i
        idx_b = len_b - 1 - i
        
        val_a = wielomian_a[idx_a] if idx_a >= 0 else 0
        val_b = wielomian_b[idx_b] if idx_b >= 0 else 0
        
        wynik.append(val_a + val_b)
    
    # Odwrócenie wyniku (aby był w formacie [a_n, ..., a_0])
    wynik.reverse()
    
    return wynik


def test_suma_wielomianow():
    assert suma_wielomianow([1, 2, 3], [1, 2, 3]) == [2, 4, 6]
    assert suma_wielomianow([1, 2, 3, 4], [5, 6]) == [1, 2, 8, 10]


if __name__ == "__main__":
    # Wczytanie dwóch wielomianów jako listy
    wielomian_a = eval(input().strip())
    wielomian_b = eval(input().strip())
    
    # Suma wielomianów
    # Złożoność czasowa: O(max(n, m))
    # Złożoność pamięciowa: O(max(n, m))
    wynik = suma_wielomianow(wielomian_a, wielomian_b)
    
    # Wypisanie wyniku jako lista
    print(str(wynik))
