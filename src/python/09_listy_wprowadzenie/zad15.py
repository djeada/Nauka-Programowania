"""
Tytul: Liczba mniejsza od najwiekszej i wieksza od wszystkich pozostalych.
Tresc: Otrzymujesz liste liczb naturalnych. Znajdz najwieksza i druga co do wielkosci liczbe w liscie, a nastepnie oblicz srednia arytmetyczna tych dwoch liczb i zwroc ja jako liczbe zmiennoprzecinkowa.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba zmiennoprzecinkowa oznaczajaca srednia arytmetyczna najwiekszej i drugiej co do wielkosci liczby z listy.
Przyklad:
Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostac zwrocona liczba 8.0.

"""


def element_dominujacy(lista):
    for element in lista:
        if lista.count(element) > len(lista) / 2:
            return element

    return -1


def test_element_dominujacy():
    assert element_dominujacy([]) == -1
    assert element_dominujacy([1]) == 1
    assert element_dominujacy([4, 7, 4, 4, 2]) == 4
    assert element_dominujacy([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1


if __name__ == "__main__":

    test_element_dominujacy()

