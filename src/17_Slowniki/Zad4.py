"""
Otrzymujesz słownik par napisów i liczb całkowitych oraz pojedynczą 
liczbę całkowitą. Usuń ze słownika pary, dla których wartość równa 
jest otrzymanej liczbie.
"""

def usun(slownik, liczba):
    """
    Funkcja usuwa ze słownika pary, dla których wartość równa jest 
    otrzymanej liczbie.
    """
    for klucz in list(slownik.keys())[:]:
        if slownik[klucz] == liczba:
            del slownik[klucz]
    return slownik

def test_usun():
    assert usun({'a': 1, 'b': 2, 'c': 3, 'd': 1}, 1) == {'b': 2, 'c': 3}
    assert usun({'a': 1, 'b': 2, 'c': 3}, 4) == {'a': 1, 'b': 2, 'c': 3}

if __name__ == "__main__":
    test_usun()    