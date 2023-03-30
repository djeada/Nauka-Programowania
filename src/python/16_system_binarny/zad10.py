"""
Tytul:  Konwersja warunkowa.
Tresc: Otrzymujesz liczbe naturalna. Zwroc reprezentacje binarna otrzymanej liczby, jesli:
a) Otrzymana liczba jest liczba parzysta.
b) Otrzymana liczba jest liczba pierwsza.
Dane wejsciowe: Liczba naturalna w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanej liczby: 7, nie powinna zostac zwrocona zadna liczba.
b) Dla otrzymanej liczby: 7, powinna zostac zwrocona liczba: 111.

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

