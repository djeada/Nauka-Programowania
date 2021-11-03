"""
Znajdź wszystkie wyjątkowe palindromy jakie można utworzyć ze znaków w słowie 
(bez zmiany kolejności występowania). Nie uwzględniaj duplikatów w liście.

Wyjątkowy palindrom musi spełniać jeden z dwóch warunków:
1. Wszystkie znaki są identyczne, np. “xxx”.
2. Wszystkie znaki poza środkowym znakiem są identyczne, np. “ccdcc”.

Pojedynczy znak jest również uznawany za wyjątkowy palindrom.
"""

def wyjatkowy_palindrom(napis):
    """
    Funkcja sprawdza czy podany napis jest wyjątkowym palindromem. 
    """
    if not napis:
        return True

    napis = napis.lower()
    if len(napis) == 1:
        return True

    if napis[0] == napis[-1]:
        return wyjatkowy_palindrom(napis[1:-1])
    
    return False

def wyjatkowe_palindromy(napis):
    """
    Funkcja zwraca wszystkie wyjątkowe palindromy, które można utworzyć z podnapisów danego napisu. 
    """
    if len(napis) == 1:
        return {napis}
    
    wynik = set()
    for i in range(len(napis)):
          for j in range(i + 1, len(napis) + 1):
                podnapis = napis[i:j]
                if wyjatkowy_palindrom(podnapis):
                    wynik.add(podnapis)

    return wynik

def test_wyjatkowy_palindrom():
    assert wyjatkowy_palindrom("xxx")
    assert wyjatkowy_palindrom("ccdcc")
    assert not wyjatkowy_palindrom("abc")

def test_wyjatkowe_palindromy():
    assert wyjatkowe_palindromy("xxxx") == {'x', 'xx', "xxx", 'xxxx'}
    assert wyjatkowe_palindromy("ccdcc") == {'cc', 'd', 'ccdcc', 'c', 'cdc'}
    assert wyjatkowe_palindromy("abc") == {"a", "b", "c"}
    assert wyjatkowe_palindromy("") == {}

if __name__ == "__main__":
    test_wyjatkowy_palindrom()
    test_wyjatkowe_palindromy()
