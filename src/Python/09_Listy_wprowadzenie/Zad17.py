"""
Dla otrzymanej listy liczb całkowitych oraz liczby x, 
znajdź wszystkie pary liczb z listy, których suma jest równa x.
"""

def znajdz_pary(lista, x):
    wynik = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == x:
                wynik.append((i, j))
    return wynik

def test_znajdz_pary():
    assert znajdz_pary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [(0, 8), (1, 7), (2, 6), (3, 5)]
    assert znajdz_pary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20) == []

if __name__ == "__main__":
    
    test_znajdz_pary()