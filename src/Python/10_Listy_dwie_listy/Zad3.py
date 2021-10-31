"""
Dla otrzymanych dwóch list, zwróć listę, której elementy są 
sumą odpowiadających sobie elementów otrzymanych list. Jeśli 
listy nie są równej długości, załóż że brakujące elementy 
krótszej listy są równe 0.
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
