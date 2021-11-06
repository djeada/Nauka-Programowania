"""
Otrzymujesz dziesiętną reprezentację liczby naturalnej. Znajdź potęgę 
dwójki większą bądź równą otrzymanej liczbie. Inaczej: zaokrąglij liczbę 
do następnej potęgi dwójki.
"""


def nastepna_potega_dwojki_v1(liczba):
    '''
    Funkcja zwraca następną potęgę dwójki większą bądź równą liczbie.
    Zasada działania opiera się na zmniejszaniu liczby, aż liczba będzie podzielna przez 2.
    '''

    if liczba <= 0:
        return 0

    if liczba == 1:
        return 2

    liczba -= 1

    while liczba & liczba - 1:
        liczba &= liczba - 1

    return liczba << 1


def nastepna_potega_dwojki_v2(liczba):
    '''
    Funkcja zwraca następną potęgę dwójki większą bądź równą liczbie.
    Zasada działania opiera się na obliczeniu następnych potęg dwójki, 
    aż otrzymamy liczbę większą lub równą podanej liczbie.
    '''

    if liczba <= 0:
        return 0

    potega = 2

    while liczba > 2:
        liczba >>= 1
        potega <<= 1

    return potega

def test_nastepna_potega_dwojki_v1():
    assert nastepna_potega_dwojki_v1(111) == 128
    assert nastepna_potega_dwojki_v1(-30) == 0
    assert nastepna_potega_dwojki_v1(1) == 2

def test_nastepna_potega_dwojki_v2():

    assert nastepna_potega_dwojki_v2(111) == 128
    assert nastepna_potega_dwojki_v2(-30) == 0
    assert nastepna_potega_dwojki_v2(1) == 2


if __name__ == "__main__":
    test_nastepna_potega_dwojki_v1()
    test_nastepna_potega_dwojki_v2()
