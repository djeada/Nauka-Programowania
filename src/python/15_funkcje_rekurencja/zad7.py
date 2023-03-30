"""
Tytul: Wieza Hanoi.
Tresc: N krazkow o roznych srednicach ulozonych jest na jednym z trzech slupkow (A, B lub C). Na dole znajduje sie krazek o najwiekszej srednicy. Kazdy nastepny jest mniejszy od poprzedniego. Znajdz sposob na przelozenie wszystkich krazkow na inny slupek. Pamietaj, ze nie wolno klasc krazka o wiekszej srednicy na krazek o mniejszej srednicy, ani przekladac kilku krazkow jednoczesnie.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Lista par znakow.
Przyklad:
Dla N = 3, powinna zostac zwrocona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]

"""


def wyszukiwani_liniowe(lista, klucz):
    """
    Funkcja zwraca indeks klucza w liscie przy pomocy rekurenkcji.
    Jesli klucz nie wystepuje w liscie, zwroc -1.
    """
    if len(lista) == 0:
        return -1

    if lista[0] == klucz:
        return 0

    if wyszukiwani_liniowe(lista[1:], klucz) != -1:
        return 1 + wyszukiwani_liniowe(lista[1:], klucz)

    return -1


def test_wyszukiwani_liniowe():
    assert wyszukiwani_liniowe([1, 2, 3, 4, 5], 3) == 2
    assert wyszukiwani_liniowe([1, 2, 3, 4, 5], 6) == -1


if __name__ == "__main__":

    test_wyszukiwani_liniowe()

