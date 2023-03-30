"""
Tytul: NWD.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najwiekszy wspolny dzielnik.
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla otrzymanych liczb 60 i 45, funkcja powinna zwrocic liczbe 15.

"""

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def test_nwd():
    assert nwd(12, 15) == 3
    assert nwd(15, 12) == 3
    assert nwd(9, 6) == 3
    assert nwd(6, 9) == 3

if __name__ == "__main__":
    test_nwd()

