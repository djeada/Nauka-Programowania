"""
Tytul: Znajdz mediane dwoch posortowanych list.
Tresc: Otrzymujesz dwie posortowane listy liczb calkowitych rownej dlugosci. Znajdz ich mediane.
Dane wejsciowe: Dwie listy liczb calkowitych o rownej dlugosci.
Dane wyjsciowe: Liczba zmiennoprzecinkowa.
Przyklad:
Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinno zostac zwrocone: 4.5.

"""

def usun_czesc_wspolna(lista_a, lista_b):
    for element in lista_a:
        if element in lista_b:
            lista_a.remove(element)
    return lista_a

def test_usun_czesc_wspolna():
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == []
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]) == [5]
    assert usun_czesc_wspolna([1, 2, 3, 4, 5], [1, 2, 3, 4, 6, 7]) == [5, 6, 7]

if __name__ == "__main__":

    test_usun_czesc_wspolna()

