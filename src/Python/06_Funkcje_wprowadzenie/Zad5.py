"""
Napisz funkcję, która dla otrzymanych dwóch liczb a oraz b zamieni wartości miejscami. 
Po wykonaniu funkcji zmienna a, powinna przechowywać dawną wartość zmiennej b, a 
zmienna b powinna przechowywać dawną wartość zmiennej a.
"""

def swap(pierwsza_liczba, druga_liczba):
    return druga_liczba, pierwsza_liczba

def test_swap():
    a, b = 1, 2
    a, b = swap(a, b)
    assert a == 2 and b == 1

if __name__ == "__main__":
    test_swap()
