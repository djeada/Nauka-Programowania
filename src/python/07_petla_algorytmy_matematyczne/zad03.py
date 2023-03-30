"""
Tytul: Mnozenie i dzielenie.
Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych a i b, przy pomocy dodawania lub odejmowania oraz petli, obliczy:
a) iloczyn tych liczb
b) iloraz liczby a przez liczbe b
Dane wejsciowe: dwie liczby naturalne
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranych liczb 3 i 2, funkcja powinna zwrocic liczbe:
a) 6;
b) 2.

"""

def iloczyn(mnozna, mnoznik):

    znak = 1

    if mnozna < 0:
        znak = -1
        mnozna = -mnozna

    if mnoznik < 0:
        znak *= -1
        mnoznik = -mnoznik

    iloczyn = 0
    for i in range(mnozna):
        iloczyn += mnoznik
    return iloczyn * znak

def iloraz(dzielna, dzielnik):
    znak = 1

    if dzielna < 0:
        znak = -1
        dzielna = -dzielna

    if dzielnik < 0:
        znak *= -1
        dzielnik = -dzielnik

    iloraz = 0
    while dzielna >= dzielnik:
        dzielna -= dzielnik
        iloraz += 1
    return iloraz * znak

def test_iloczyn():
    assert iloczyn(5, 3) == 15
    assert iloczyn(2, 3) == 6
    assert iloczyn(-2, 3) == -6
    assert iloczyn(2, -3) == -6
    assert iloczyn(-2, -3) == 6

def test_iloraz():
    assert iloraz(5, 3) == 1
    assert iloraz(2, 3) == 0
    assert iloraz(-2, 3) == 0
    assert iloraz(6, -3) == -2
    assert iloraz(-2, -3) == 0

if __name__ == "__main__":
    test_iloczyn()
    test_iloraz()

