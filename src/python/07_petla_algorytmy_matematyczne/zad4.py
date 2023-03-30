"""
Tytul: Silnia.
Tresc: Napisz funkcje, ktora obliczy silnie otrzymanej liczby naturalnej, przy pomocy petli.
Dane wejsciowe: liczba naturalna
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanej liczby 3, funkcja powinna zwrocic liczbe 6.

"""

def silnia(n):
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6
    assert silnia(4) == 24
    assert silnia(5) == 120

if __name__ == "__main__":

    test_silnia()

