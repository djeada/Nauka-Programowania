"""
Otrzymujesz dwie listy liczb całkowitych. Znajdź elementy występujące 
zarówno w pierwszej jak i w drugiej liście.
"""

def czesc_wspolna(lista_a, lista_b):
    return [x for x in lista_a if x in lista_b]

def test_czesc_wspolna():
    assert set(czesc_wspolna([3, 6, 2, 7, 9], [4, 2, 3, 5, 6])) == set([3, 6, 2])
    assert set(czesc_wspolna([1, 2, 3, 4], [2, 3, 4, 5, 6])) == set([2, 3, 4])


if __name__ == "__main__":
    test_czesc_wspolna()
    