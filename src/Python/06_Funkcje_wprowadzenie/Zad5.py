"""
Napisz funkcje, ktora dla otrzymanych dwoch liczb a oraz b zamieni wartosci miejscami. 
Po wykonaniu funkcji zmienna a, powinna przechowywac dawna wartosc zmiennej b, a 
zmienna b powinna przechowywac dawna wartosc zmiennej a.
"""


def swap(pierwsza_liczba, druga_liczba):
    '''
    Funkcja zamienia wartosci miejscami.
    '''
    return druga_liczba, pierwsza_liczba


def test_swap():
    a, b = 1, 2
    a, b = swap(a, b)
    assert a == 2 and b == 1


if __name__ == "__main__":
    test_swap()
