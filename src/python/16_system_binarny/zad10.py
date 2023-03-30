"""
Tytul: Zamien A na B.
Tresc: Otrzymujesz dwie liczby naturalne. Oblicz, ile bitow nalezy odwrocic, aby zamienic liczbe A na liczbe B.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych liczb 34 i 73, powinna zostac zwrocona liczba 5.

"""

def bity_do_zmiany(liczba_a, liczba_b):
    """
    Funkcja zwraca ilosc bitow do zmiany liczby A w liczbe B.
    """

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

