"""
Tytul: Czy slowniki sa identyczne?
Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. Listy sa nieuporzadkowane. Twoim zadaniem jest sprawdzenie, czy slowniki skladaja sie z tych samych par. Dwie listy uznajemy za identyczne, jesli zawieraja te same elementy, niezaleznie od kolejnosci, w jakiej sie one znajduja.
Dane wejsciowe: Dwa slowniki par: napis, lista liczb calkowitych.
Dane wyjsciowe: Wartosc boolowska.
Przyklad:
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}
Powinna zostac zwrocona wartosc logiczna: Prawda.
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}
Powinna zostac zwrocona wartosc logiczna: Falsz.

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

