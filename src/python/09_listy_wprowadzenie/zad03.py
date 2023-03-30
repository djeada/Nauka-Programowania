"""
Tytul: Pierwsze wystapienie klucza.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna jako klucz. Znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.
Dane wyjsciowe: Liczba calkowita oznaczajaca indeks pierwszego wystapienia klucza w liscie.
Przyklad:
Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostac zwrocone 2.

"""

def znajdz_klucz(lista, klucz):

    for i in range(len(lista)):
        if lista[i] == klucz:
            return i
    return -1

def test_znajdz_klucz():
    assert znajdz_klucz([1, 2, 3, 4, 5], 5) == 4
    assert znajdz_klucz([1, 2, 3, 4, 5], 6) == -1

if __name__ == "__main__":

    test_znajdz_klucz()

