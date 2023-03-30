"""
Tytul: Liczba zer i jedynek w reprezentacji binarnej.
Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej.
a) Oblicz, ile zer zawiera binarna reprezentacja otrzymanej liczby.
b) Oblicz, ile jedynek zawiera binarna reprezentacja otrzymanej liczby.
Dane wejsciowe: Liczba naturalna w obu podpunktach.
Dane wyjsciowe: Liczba naturalna w obu podpunktach.
Przyklad:
a) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 0.
b) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 2.

"""


def najdluzszy_ciag_zer(liczba):
    """
    Funkcja zwraca dlugosc najdluzszego ciagu zer w dziesietnej
    reprezentacji liczby binarnej.
    """
    liczba_bin = bin(liczba)
    liczba_bin = liczba_bin[2:]
    liczba_bin = liczba_bin.split("1")
    liczba_bin.sort(key=len)
    return len(liczba_bin[-1])


def test_najdluzszy_ciag_zer():
    assert najdluzszy_ciag_zer(0) == 1
    assert najdluzszy_ciag_zer(111) == 1
    assert najdluzszy_ciag_zer(8219) == 8


if __name__ == "__main__":

    test_najdluzszy_ciag_zer()

