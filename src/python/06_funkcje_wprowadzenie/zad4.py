"""
Tytul: Maks i min
Napisz funkcje, ktora:
a) Dla otrzymanych dwoch liczb zwroci mniejsza.
b) Dla otrzymanych dwoch liczb zwroci wieksza.
c) Dla otrzymanych trzech liczb zwroci najmniejsza.
d) Dla otrzymanych trzech liczb zwroci najwieksza.
Dane wejsciowe:
a) Dwie liczby naturalne.
b) Dwie liczby naturalne.
c) Trzy liczby naturalne.
d) Trzy liczby naturalne.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
a) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 1.
b) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 3.
c) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 1.
d) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 3."

"""

def min_2(a, b):
    """
    Funkcja zwraca mniejsza z dwoch liczb.
    """
    if a < b:
        return a
    else:
        return b

def maks_2(a, b):
    """
    Funkcja zwraca wieksza z dwoch liczb.
    """
    if a > b:
        return a
    else:
        return b

def min_3(a, b, c):
    """
    Funkcja zwraca najmniejsza z trzech liczb.
    """
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

def maks_3(a, b, c):
    """
    Funkcja zwraca najwieksza z trzech liczb.
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def test_min_2():
    assert min_2(1, 2) == 1
    assert min_2(2, 1) == 1
    assert min_2(2, 2) == 2

def test_maks_2():
    assert maks_2(1, 2) == 2
    assert maks_2(2, 1) == 2
    assert maks_2(2, 2) == 2

def test_min_3():
    assert min_3(1, 2, 3) == 1
    assert min_3(2, 1, 3) == 1
    assert min_3(3, 1, 2) == 1
    assert min_3(2, 3, 1) == 1
    assert min_3(3, 2, 1) == 1
    assert min_3(1, 3, 2) == 1

def test_maks_3():
    assert maks_3(1, 2, 3) == 3
    assert maks_3(2, 1, 3) == 3
    assert maks_3(3, 1, 2) == 3
    assert maks_3(2, 3, 1) == 3
    assert maks_3(3, 2, 1) == 3
    assert maks_3(1, 3, 2) == 3

if __name__ == "__main__":

    test_min_2()
    test_maks_2()
    test_min_3()
    test_maks_3()

