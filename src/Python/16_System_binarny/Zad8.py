"""
znajdz potege 2 wieksza badz rowna liczbie. inaczej: zaaokraglij liczbe do nastepnej potegi 2.
dla podanej liczby ujemnej zwroc 0.
"""


# zmniejszaj az x bedzie poprzednia potega dwojki
def nastepna_potega_dwojki_v1(liczba):

    if liczba <= 0:
        return 0

    if liczba == 1:
        return 2

    liczba -= 1

    while liczba & liczba - 1:
        liczba &= liczba - 1

    return liczba << 1


# compute power of two greater than or equal to n
def nastepna_potega_dwojki_v2(liczba):

    if liczba <= 0:
        return 0

    potega = 2

    while liczba > 2:
        liczba >>= 1
        potega <<= 1

    return potega


if __name__ == "__main__":

    liczba = 111
    wynik = 128

    assert nastepna_potega_dwojki_v1(liczba) == wynik
    assert nastepna_potega_dwojki_v2(liczba) == wynik

    liczba = -30
    wynik = 0

    assert nastepna_potega_dwojki_v1(liczba) == wynik
    assert nastepna_potega_dwojki_v2(liczba) == wynik

    liczba = 1
    wynik = 2

    assert nastepna_potega_dwojki_v1(liczba) == wynik
    assert nastepna_potega_dwojki_v2(liczba) == wynik
