"""
Dla otrzymanej listy liczb naturalnych, znajdź element dominujący. 
Element dominujący to element, którego liczba wystąpień w liście 
jest większa niż połowa długości listy. Jeśli lista nie ma 
elementu dominującego, zwróć -1.
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
