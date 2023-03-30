"""
Tytul: Mnozenie wektorowe.
Tresc: Tresc: Otrzymujesz dwie listy liczb calkowitych reprezentujace dwa wektory trojwymiarowej przestrzeni euklidesowej. Zaimplementuj mnozenie wektorowe (zdefiniowane jedynie dla wektorow 3-wymiarowej przestrzeni euklidesowej).
Dane wejsciowe: Dwie listy liczb calkowitych o dlugosci 3.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanych list [1, 2, 3] oraz [3, 1, 2], powinno zostac zwrocone: 5.

"""

def suma_list(lista_a, lista_b):
    if len(lista_a) > len(lista_b):
        lista_b = lista_b + [0] * (len(lista_a) - len(lista_b))
    elif len(lista_a) < len(lista_b):
        lista_a = lista_a + [0] * (len(lista_b) - len(lista_a))
    return [a + b for a, b in zip(lista_a, lista_b)]

def test_suma_list():
    assert suma_list([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert suma_list([1, 2, 3], [4, 5]) == [5, 7, 3]

if __name__ == "__main__":

    test_suma_list()

