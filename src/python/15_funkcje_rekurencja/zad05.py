"""
Tytul: Liczba Fibonacciego.
Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji oblicz wartosc N-tego wyrazu ciagu Fibonacciego.
Podpowiedz: Ciag Fibonacciego zdefiniowany jest nastepujaco:
* $a_0= 0$,
* $a_1= 1$,
* $a_n= a_{n-1}+a_n-2$.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla N = 7, powinna zostac zwrocona liczba: 13.

"""


def wyraz_ciag_fibonacciego(n):
    """
    Funkcja oblicza n-ty wyraz ciagu Fibonacciego.
    """
    if n < 0:
        raise ValueError("Liczba musi byc nieujemna")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    return wyraz_ciag_fibonacciego(n - 1) + wyraz_ciag_fibonacciego(n - 2)


def test_wyraz_ciag_fibonacciego():
    assert wyraz_ciag_fibonacciego(0) == 0
    assert wyraz_ciag_fibonacciego(1) == 1
    assert wyraz_ciag_fibonacciego(12) == 144


if __name__ == "__main__":

    test_wyraz_ciag_fibonacciego()
