"""
Napisz funkcję, która dla otrzymanych dwóch liczb przy 
pomocy pętli obliczy ile wynosi a podniesione do b.
"""


def potega(podstawa, wykladnik):
    wynik = 1
    for i in range(wykladnik):
        wynik *= podstawa
    return wynik


def test_potega():
    assert potega(2, 3) == 8
    assert potega(3, 2) == 9
    assert potega(4, 4) == 256
    assert potega(5, 3) == 125
    assert potega(6, 0) == 1
    assert potega(7, 1) == 7
    assert potega(0, 2) == 0


if __name__ == "__main__":

    test_potega()
