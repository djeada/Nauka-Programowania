"""
Tytul: Rotacja w lewo/prawo.
Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesun elementy listy w podanym kierunku.
Dane wejsciowe: Lista liczb calkowitych oraz dwie liczby naturalne.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac zwrocona lista: [6, 2, 1, 10, 8, 5, 27].

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

