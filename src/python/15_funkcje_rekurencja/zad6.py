"""
Tytul: Wyszukiwanie liniowe rekurencyjnie.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna klucz. Przy uzyciu rekurencji znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna klucz.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy oraz liczby: [1, 2, 2] i 2, powinna zostac zwrocona liczba: 1.

"""

def wyraz_ciag(n):
    """
    Funkcja oblicza n-ty wyraz ciagu danego wzorem rekurencyjnym:
    a_1 = 1,
    a_n = 1 + 2a_(n-1)
    """
    if n < 1:
        raise ValueError("Liczba musi byc wieksza od zera")

    if n == 1:
        return 1
    else:
        return 1 + 2 * wyraz_ciag(n - 1)

def test_wyraz_ciag():

    assert wyraz_ciag(1) == 1
    assert wyraz_ciag(2) == 3
    assert wyraz_ciag(10) == 1023

if __name__ == "__main__":
    test_wyraz_ciag()

