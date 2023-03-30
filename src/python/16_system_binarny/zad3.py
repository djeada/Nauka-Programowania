"""
Tytul:  Konwersja miedzy dowolnymi systemami liczbowymi.
Tresc: Otrzymujesz liczbe naturalna, podstawe systemu liczbowego, w ktorym zapisana jest ta liczba, oraz podstawe systemu, na ktory ma zostac dokonana konwersja. Zwroc reprezentacje otrzymanej liczby w nowym systemie.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych liczb: 4301, 10 i 4 powinna zostac zwrocona liczba: 1003031.

"""


def suma(a, b):
    """
    Funkcja dodaje dwie liczby naturalne.
    """
    while b != 0:
        pom = a & b
        a = a ^ b
        b = pom << 1

    return a


def roznica(a, b):
    """
    Funkcja odejmuje dwie liczby naturalne.
    """
    while b != 0:
        pom = (~a) & b
        a = a ^ b
        b = pom << 1

    return a


def iloczyn(a, b):
    """
    Funkcja mnozy dwie liczby naturalne.
    """
    znak = -1 if (a < 0 and b >= 0) or (b < 0 and a >= 0) else 1

    a = abs(a)
    b = abs(b)

    pom = 0
    while b != 0:
        if b & 1:
            pom = suma(pom, a)
        a = a << 1
        b = b >> 1

    return znak * pom


def iloraz(a, b):
    """
    Funkcja zwraca iloraz a przez b, gdzie a i b sa liczbami naturalnymi.
    """

    if b == 0:
        raise ZeroDivisionError

    znak = -1 if (a < 0 and b >= 0) or (b < 0 and a >= 0) else 1

    a = abs(a)
    b = abs(b)

    def wew_iloraz(dzielna, dzielnik, org_b):
        """
        Funkcja wewnetrzna funkcji iloraz.
        """
        wynik = 1

        if dzielna == dzielnik:
            return 1

        elif dzielna < dzielnik:
            return 0

        while dzielnik <= dzielna:
            dzielnik = dzielnik << 1
            wynik = wynik << 1

        if dzielna < dzielnik:
            dzielnik >>= 1
            wynik >>= 1

        wynik += wew_iloraz(dzielna - dzielnik, org_b, org_b)

        return wynik

    return znak * wew_iloraz(a, b, b)


def test_suma():
    assert suma(1, 1) == 2
    assert suma(5, 3) == 8
    assert suma(0, 0) == 0


def test_roznica():
    assert roznica(1, 1) == 0
    assert roznica(5, 3) == 2
    assert roznica(0, 0) == 0


def test_iloczyn():
    assert iloczyn(1, 1) == 1
    assert iloczyn(5, 3) == 15
    assert iloczyn(0, 0) == 0
    assert iloczyn(-3, 2) == -6
    assert iloczyn(-3, -2) == 6
    assert iloczyn(3, -2) == -6


def test_iloraz():
    assert iloraz(1, 1) == 1
    assert iloraz(9, 3) == 3
    assert iloraz(-3, 2) == -1
    assert iloraz(-3, -2) == 1
    assert iloraz(3, -2) == -1


if __name__ == "__main__":

    test_suma()
    test_roznica()
    test_iloczyn()
    test_iloraz()

