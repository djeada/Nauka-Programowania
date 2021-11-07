"""
Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza 
liczbe calkowita. Usun ze slownika pary, dla ktorych wartosc rowna 
jest otrzymanej liczbie.
"""


def usun(slownik, liczba):
    """
    Funkcja usuwa ze slownika pary, dla ktorych wartosc rowna jest 
    otrzymanej liczbie.
    """
    for klucz in list(slownik.keys())[:]:
        if slownik[klucz] == liczba:
            del slownik[klucz]
    return slownik


def test_usun():
    assert usun({"a": 1, "b": 2, "c": 3, "d": 1}, 1) == {"b": 2, "c": 3}
    assert usun({"a": 1, "b": 2, "c": 3}, 4) == {"a": 1, "b": 2, "c": 3}


if __name__ == "__main__":
    test_usun()
