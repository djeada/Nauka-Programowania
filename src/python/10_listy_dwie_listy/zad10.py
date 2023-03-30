"""
Tytul: Znajdz mediane dwoch posortowanych list.
Tresc: Otrzymujesz dwie posortowane listy liczb calkowitych rownej dlugosci. Znajdz ich mediane.
Dane wejsciowe: Dwie listy liczb calkowitych o rownej dlugosci.
Dane wyjsciowe: Liczba zmiennoprzecinkowa.
Przyklad:
Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinno zostac zwrocone: 4.5.

"""

def mediana_list(lista_a, list_b):
    lista_a.extend(list_b)
    lista_a.sort()
    return lista_a[len(lista_a) // 2]

def test_mediana_list():
    assert mediana_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 7
    assert mediana_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]) == 8

if __name__ == "__main__":

    test_mediana_list()

