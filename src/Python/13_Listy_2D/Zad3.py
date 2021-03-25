"""
Otrzymujesz dwie listy 1-wymiarowe. Stworz liste 2D z par odpowiadajacych sobie elementow obu list.
Zwroc -1 jesli listy sa roznej dlugosci.
"""

# Wersja 1
def polaczParyV1(listaA, listaB):
    if len(listaA) == len(listaB):
        return -1

    return [(a, b) for a, b in zip(listaA, listaB)]


# Testy Poprawnosci
listaA = [3, 2, 9]
listaB = [1, 7, -2]
wynik = [(3, 1), (2, 7), (9, -2)]
