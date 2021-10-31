"""
Dla otrzymanej listy liczb naturalnych znajdź 
średnią arytmetyczną największej i drugiej największej 
liczby w liście.
"""

def srednia_dwoch_najwiekszych(lista):
    
    if len(lista) < 2:
        return 0.00

    najwieksza = max(lista)
    najwieksza_druga = max(lista[:lista.index(najwieksza)])
    srednia = (najwieksza + najwieksza_druga) / 2
    return srednia

def test_srednia_dwoch_najwiekszych():

    assert srednia_dwoch_najwiekszych([]) == 0.00
    assert srednia_dwoch_najwiekszych([1]) == 0.00
    assert srednia_dwoch_najwiekszych([1, 2]) == 1.50
    assert srednia_dwoch_najwiekszych([3, 5, -7, 4, 9, -11, 2]) == 7.00
    assert srednia_dwoch_najwiekszych([3, -2, 4, 9, -3, -40, 8, 5, -7, 4, 9, -11, 2]) == 6.5

if __name__ == "__main__":
    
    test_srednia_dwoch_najwiekszych()