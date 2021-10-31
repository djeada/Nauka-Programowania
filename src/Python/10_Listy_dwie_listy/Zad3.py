"""
Dla otrzymanych dwoch list, zwroc liste, ktorej elementy sa 
suma odpowiadajacych sobie elementow otrzymanych list. Jesli 
listy nie sa rownej dlugosci, zaloz ze brakujace elementy 
krotszej listy sa rowne 0.
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
