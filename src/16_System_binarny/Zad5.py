'''
Otrzymujesz dwie liczby naturalne. 

a) Zwróć mniejszą liczbę. Zabronione jest użycie instrukcji 
warunkowej i zewnętrznych bibliotek.
b) Zwróć większą liczbę. Zabronione jest użycie instrukcji 
warunkowej i zewnętrznych bibliotek.
'''

def znak(n):
    '''
    Funkcja zwraca znak liczby n.
    '''
    return (n >> 31) & 0x01

def maksimum(a, b):
    '''
    Funkcja zwraca maksimum dwóch liczb.
    dla a >= b: znak_a = 1, znak_b = 0;
    dla a < b: znak_a = 0, znak_b = 1;
    '''
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_a * a + znak_b * b


def minimum(a, b):
    '''
    Funkcja zwraca minimum dwóch liczb.
    dla a >= b: znak_a = 0, znak_b = 1;
    dla a < b: znak_a = 1, znak_b = 0;
    '''
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_b * a + znak_a * b

def test_maksimum():
    assert maksimum(2, 3) == 3
    assert maksimum(3, 2) == 3
    assert maksimum(3, 3) == 3
    assert maksimum(0, 0) == 0
    assert maksimum(-2, -3) == -2
    assert maksimum(-3, -2) == -2
    assert maksimum(-3, -3) == -3

def test_minimum():
    assert minimum(2, 3) == 2
    assert minimum(3, 2) == 2
    assert minimum(3, 3) == 3
    assert minimum(0, 0) == 0
    assert minimum(-2, -3) == -3
    assert minimum(-3, -2) == -3
    assert minimum(-3, -3) == -3


if __name__ == "__main__":

    test_minimum()
    test_maksimum()
