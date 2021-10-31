"""
Dla otrzymanej listy znajdź indeks najmniejszego elementu. Lista jest posortowana 
rosnąco,  ale została przesunięta. Przykładowo dla przesunięcie w prawo o 1, 
ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.
"""

def znajdz_min_indeks(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            return i + 1

    return 0
    
def test_znajdz_min_indeks():
    assert  znajdz_min_indeks([7, 8, -1, 4, 5]) == 2
    assert  znajdz_min_indeks([2, 3, 4, 5, 6]) == 0
    assert  znajdz_min_indeks([8, 9, 10, 11, 1]) == 4


if __name__ == "__main__":
    
    test_znajdz_min_indeks()