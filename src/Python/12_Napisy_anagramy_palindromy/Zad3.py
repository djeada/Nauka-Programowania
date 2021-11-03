"""
Dla podanych dwóch napisów sprawdź czy są swoimi anagramami. 
Dwa napisy są anagramami jeśli jeden z nich można zbudować 
poprzez przestawienie znaków w drugim.
"""

def anagramy(napis_a, napis_b):
    """
    Funkcja sprawdza czy dane napisy są anagramami.
    """
    if len(napis_a) != len(napis_b):
        return False

    for znak in napis_a:
        if napis_a.count(znak) != napis_b.count(znak):
            return False

    return True

def test_anagramy():
    assert anagramy('kajak', 'kajak')
    assert not anagramy('kajak', 'kjakk')
    assert anagramy('adam', 'mada')

if __name__ == "__main__":
    test_anagramy()