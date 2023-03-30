"""
Tytul: NWW.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najmniejsza wspolna wielokrotnosc.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanych liczb 7 i 9, funkcja powinna zwrocic liczbe 63.

"""

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return a * b // nwd(a, b)

def test_nww():
    assert nww(12, 15) == 60
    assert nww(12, 16) == 48
    assert nww(12, 18) == 36

if __name__ == "__main__":

    test_nww()

