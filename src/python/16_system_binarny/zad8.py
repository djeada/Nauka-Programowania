"""
Tytul: Czy liczba jest palindromem?
Tresc: Otrzymujesz dziesietna reprezentacje liczby naturalnej. Sprawdz, czy reprezentacja binarna otrzymanej liczby jest palindromem.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla otrzymanej liczby 26, powinna zostac zwrocona wartosc logiczna: Prawda.

"""

def nastepna_potega_dwojki_v1(liczba):
    """
    Funkcja zwraca nastepna potege dwojki wieksza badz rowna liczbie.
    Zasada dzialania opiera sie na zmniejszaniu liczby, az liczba bedzie podzielna przez 2.
    """

    if liczba <= 0:
        return 0

    if liczba == 1:
        return 2

    liczba -= 1

    while liczba & liczba - 1:
        liczba &= liczba - 1

    return liczba << 1

def nastepna_potega_dwojki_v2(liczba):
    """
    Funkcja zwraca nastepna potege dwojki wieksza badz rowna liczbie.
    Zasada dzialania opiera sie na obliczeniu nastepnych poteg dwojki,
    az otrzymamy liczbe wieksza lub rowna podanej liczbie.
    """

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

