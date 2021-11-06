
"""
Otrzymujesz słownik składający się z par napisów i liczb całkowitych. 
a) Wypisz pary posortowane względem napisów.
b) Wypisz pary posortowane względem liczb.
"""

def sortuj_wzgledem_kluczy(slownik):
    '''
    Funkcja sortuje słownik względem kluczy.
    '''
    return sorted(slownik.items(), key=lambda x: x[0])

def sortuj_wzgledem_wartosci(slownik):
    '''	
    Funkcja sortuje słownik względem wartości.
    '''
    return sorted(slownik.items(), key=lambda x: x[1])
    
def test_sortuj_wzgledem_kluczy():
    assert sortuj_wzgledem_kluczy({'a': 2, 'c': 1, 'b': 3, }) == [('a', 2), ('b', 3), ('c', 1)]

def test_sortuj_wzgledem_wartosci():
    assert sortuj_wzgledem_wartosci({'a': 2, 'c': 1, 'b': 3, }) == [('c', 1), ('a', 2), ('b', 3)]


if __name__ == "__main__":
    
    test_sortuj_wzgledem_kluczy()
    test_sortuj_wzgledem_wartosci()
