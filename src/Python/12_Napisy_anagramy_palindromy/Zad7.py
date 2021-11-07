"""
Dla dwoch slow, ile minimalnie znakow musimy usunac aby uzyskac anagramy.
Zwroc -1 dla slow o roznych dlugosciach.
"""


def liczba_znakow(napis_a, napis_b):
    """
    Funkcja zwraca liczbe znakow, ktore musimy usunac aby uzyskac anagramy. 
    """
    if len(napis_a) != len(napis_b):
        return -1

    pom = [0] * 256

    for znak in napis_a:
        pom[ord(znak) - ord("a")] += 1

    for znak in napis_b:
        pom[ord(znak) - ord("a")] -= 1

    return sum(map(abs, pom))


def test_liczba_znakow():
    assert liczba_znakow("grazyna", "razynax") == 2
    assert liczba_znakow("pan cytryna", "pan pomarancza") == -1
    assert liczba_znakow("20ejdy0978oa", "akv81w39j1ob") == 14


if __name__ == "__main__":

    test_liczba_znakow()
