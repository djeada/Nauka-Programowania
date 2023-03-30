"""
Tytul: Usuwanie z slownika.
Tresc: Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza liczbe calkowita. Usun z slownika pary, dla ktorych wartosc jest rowna otrzymanej liczbie.
Dane wejsciowe: Slownik par napisow i liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Slownik par napisow i liczb calkowitych.
Przyklad:
Dla slownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, slownik powinien wygladac nastepujaco: {“abc”: 1, “cba” : 3}.

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

