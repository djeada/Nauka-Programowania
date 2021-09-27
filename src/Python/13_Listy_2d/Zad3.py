"""
Otrzymujesz dwie listy 1-wymiarowe. Stworz liste 2D z par odpowiadajacych sobie elementow obu list.
Zwroc -1 jesli listy sa roznej dlugosci.
"""

# Wersja 1
def polacz_pary_v1(lista_a, lista_b):
    if len(lista_a) == len(lista_b):
        return -1

    return [(a, b) for a, b in zip(lista_a, lista_b)]


# Testy Poprawnosci
lista_a = [3, 2, 9]
lista_b = [1, 7, -2]
wynik = [(3, 1), (2, 7), (9, -2)]
