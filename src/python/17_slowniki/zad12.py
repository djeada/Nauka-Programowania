"""
Tytul: Usuwanie z slownika.
Tresc: Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza liczbe calkowita. Usun z slownika pary, dla ktorych wartosc jest rowna otrzymanej liczbie.
Dane wejsciowe: Slownik par napisow i liczb calkowitych oraz liczba calkowita.
Dane wyjsciowe: Slownik par napisow i liczb calkowitych.
Przyklad:
Dla slownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, slownik powinien wygladac nastepujaco: {“abc”: 1, “cba” : 3}.

"""

def czy_slowniki_identyczne(slownik_a, slownik_b):
    """
    Funkcja sprawdza czy dwa slowniki maja takie same elementy.
    """
    for klucz in slownik_a:
        if klucz not in slownik_b:
            return False
        elif sorted(slownik_a[klucz]) != sorted(slownik_b[klucz]):
            return False
    return True

def test_czy_slowniki_identyczne():

    assert czy_slowniki_identyczne(
        {"a": [1, 2, 3], "b": [4, 5, 6]}, {"a": [3, 1, 2], "b": [5, 4, 6]}
    )

if __name__ == "__main__":

    test_czy_slowniki_identyczne()

