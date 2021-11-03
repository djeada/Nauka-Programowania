import string

"""
Dla otrzymanych dwóch list, stwórz dwukolumnową macierz, której pierwsza 
kolumna składa się z elementów pierwszej listy, a druga kolumna elementów 
drugiej listy. Jeśli otrzymane listy nie są równej długości zwróć pustą macierz.
"""

def polacz_listy_w_macierz(lista_a, lista_b):
    """	
    Funkcja zwraca macierz dwuwymiarową, której pierwsza kolumna składa się z
    elementów pierwszej listy, a druga kolumna elementów drugiej listy. 
    Jeśli otrzymane listy nie są równej długości zwróć pustą macierz.
    """	
    if len(lista_a) != len(lista_b):
        return []
    macierz = []
    for element_a, element_b in zip(lista_a, lista_b):
        macierz.append(element_a, element_b)
    return macierz

def test_polacz_listy_w_macierz():
    assert polacz_listy_w_macierz([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]
    assert polacz_listy_w_macierz([1, 2, 3], [4, 5]) == []


if __name__ == "__main__":
    test_polacz_listy_w_macierz()