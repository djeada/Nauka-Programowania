"""
Polacz m posortowanych list.
Elementy sa unikalne.
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
def polaczListyV1(lista):

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
def polaczListyV2(lista):
    return sorted([x for y in lista for x in y])


if __name__ == "__main__":

    lista = [[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]

    wynik = [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]

    print(polaczListyV1(lista))

    assert polaczListyV1(lista) == wynik
    assert polaczListyV2(lista) == wynik
