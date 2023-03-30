"""
Tytul: Liczby naturalne mniejsze od N.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji stworz napis skladajacy sie z liczb naturalnych mniejszych od N oddzielonych przecinkami.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Napis.
Przyklad:
Dla N = 10, powinien zostac zwrocony napis: "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0".

"""

def liczby(n):
    """
    Funkcja zwraca napis skladajacy sie z liczb naturalnych
    mniejszych od podanej liczby n.
    """

    if n <= 0:
        return ""

    if n == 1:
        return "1"
    else:
        return str(n) + ", " + liczby(n - 1)

def test_liczby():

    assert liczby(0) == ""
    assert liczby(10) == "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"

if __name__ == "__main__":

    test_liczby()

