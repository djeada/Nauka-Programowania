"""
Otrzymujesz liste 2d skladajaca sie z M posortowanych list. Polacz otrzymane listy w
jedna posortowana liste. Wszystkie elementy sa unikalne.
"""

import heapq


class Node(object):
    def __init__(self, val: int, i: int, index: int):
        self.val = val
        self.i = i
        self.index = index

    def __lt__(self, other):
        return self.val < other.val


# Zlozonosc czasowa: O(nlogm)
# Zalozenie pop/push O(logm)
def polacz_listy_v1(lista):

    M = len(lista)

    heap = [Node(lista[i][0], i, 0) for i in range(M) if len(lista[i]) >= 1]
    heapq.heapify(heap)
    wynik = []

    while len(heap) > 0:

        min = heapq.heappop(heap)
        wynik.append(min.val)

        if min.index + 1 < len(lista[min.i]):
            min.index += 1
            min.val = lista[min.i][min.index]
            heapq.heappush(heap, min)

    return wynik


# Zlozonosc czasowa: O(n^2)
def polacz_listy_v2(lista):
    return sorted([x for y in lista for x in y])


# Testy Poprawnosci
def test_1():
    lista = [[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
    wynik = [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]

    assert polacz_listy_v1(lista) == wynik
    assert polacz_listy_v2(lista) == wynik


def test_2():
    lista = [[1, 2, 3], [4, 5, 6]]
    wynik = [1, 2, 3, 4, 5, 6]

    assert polacz_listy_v1(lista) == wynik
    assert polacz_listy_v2(lista) == wynik


def test_3():
    lista = [[]]
    wynik = []

    assert polacz_listy_v1(lista) == wynik
    assert polacz_listy_v2(lista) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()
