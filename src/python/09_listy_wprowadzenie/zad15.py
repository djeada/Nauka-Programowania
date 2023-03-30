"""
Tytul: Znalezienie elementu dominujacego w liscie liczb naturalnych.
Tresc: Dla dostarczonej listy liczb naturalnych, znajdz element, ktory wystepuje w niej wiecej niz polowa jej dlugosci. Jesli taki element nie istnieje, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrocona liczba: 4.

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

