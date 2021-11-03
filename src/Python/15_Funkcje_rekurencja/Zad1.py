"""
Otrzymujesz liczbę N. Przy użyciu rekurencji zbuduj napis składający 
się z liczb naturalnych mniejszych od N oddzielonych przecinkami.
"""

def liczby(n):
    """
    Funkcja zwraca napis składający się z liczb naturalnych 
    mniejszych od podanej liczby n.
    """

    if n <= 0:
        return ""

    if n == 1:
        return '1'	
    else:
        return str(n) + ", " + liczby(n-1)


def test_liczby():

    assert liczby(0) == ""
    assert liczby(10) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"

if __name__ == "__main__":
    
    test_liczby()
