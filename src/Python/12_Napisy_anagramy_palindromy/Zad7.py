"""
Dla dwóch słów, ile minimalnie znaków musimy usunąć aby uzyskać anagramy.
Zwróć -1 dla słów o różnych długościach.
"""


def liczba_znakow(napis_a, napis_b):
    """
    Funkcja zwraca liczbę znaków, które musimy usunąć aby uzyskać anagramy. 
    """
    if len(napis_a) != len(napis_b):
        return -1

    pom = [0] * 256

    for znak in napis_a:
        pom[ord(znak) - ord('a')] += 1
        
    for znak in napis_b:
        pom[ord(znak) - ord('a')] -= 1

    return sum(map(abs, pom))


def test_liczba_znakow():
    assert liczba_znakow("grazyna", "razynax") == 2
    assert liczba_znakow("pan cytryna", "pan pomarancza") == -1
    assert liczba_znakow("20ejdy0978oa", "akv81w39j1ob") == 14

if __name__ == "__main__":
    
    test_liczba_znakow()