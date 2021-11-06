"""
Otrzymujesz dwie liczby naturalne. Oblicz ile bitów 
należy odwrócić, aby zamienić liczbę A w liczbę B.  
"""


def bity_do_zmiany(liczba_a, liczba_b):
    '''
    Funkcja zwraca ilość bitów do zmiany liczby A w liczbę B.
    '''

    n = liczba_a ^ liczba_b

    licznik_jedynek = 0
    while n:
        n &= n - 1
        licznik_jedynek += 1

    return licznik_jedynek


def test_bity_do_zmiany():
    assert bity_do_zmiany(0, 0) == 0
    assert bity_do_zmiany(1, 2) == 31
    assert bity_do_zmiany(34, 73) == 5

if __name__ == "__main__":

    test_bity_do_zmiany()

