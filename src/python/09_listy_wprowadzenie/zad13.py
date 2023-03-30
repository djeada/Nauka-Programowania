"""
Tytul: Zmodyfikuj elementy spelniajace warunek.
Tresc: Otrzymujesz liste liczb calkowitych. W wyniku wykonania ponizszych polecen otrzymasz nowa liste:
a) Zwieksz o 1 wszystkie elementy o parzystych indeksach (indeksy zaczynaja sie od 0).
b) Wyzeruj wszystkie elementy bedace wielokrotnosciami liczby 3.
c) Podnies do kwadratu wszystkie elementy mniejsze niz 10.
d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
e) Zamien kazdy element na iloczyn wszystkich elementow listy poza nim samym.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych.
Przyklad:
Dla otrzymanej listy [5, 7, 9, 4, 2]:
a) Wynik: [5, 8, 9, 5, 2]
b) Wynik: [5, 0, 0, 5, 2]
c) Wynik: [25, 0, 0, 25, 4]
d) Wynik: [37, 0, 0, 25, 4]
e) Wynik: [2592, 0, 0, 36, 1080]

"""


def suma_ciag_aryt(lista):
    return (len(lista) + 1) * (min(lista) + max(lista)) // 2


def brakujacy_element(lista):

    suma_przedzialu = suma_ciag_aryt(lista)
    suma_listy = sum(lista)

    wynik = suma_przedzialu - suma_listy

    if wynik not in lista:
        return wynik

    return 0


def test_brakujacy_element():
    assert brakujacy_element([6, 8, 4, 10, 14, 2]) == 12
    assert brakujacy_element([1, 2, 4, 5, 6]) == 3
    assert brakujacy_element([1, 2, 3]) == 0


if __name__ == "__main__":

    test_brakujacy_element()

