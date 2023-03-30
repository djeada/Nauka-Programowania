"""
Tytul: Polaczone posortowane listy
Tresc: Otrzymujesz liste zawierajaca M posortowanych list. Polacz te listy w jedna posortowana liste. Wszystkie elementy sa unikalne.
Dane wejsciowe: Lista list zawierajacych liczby naturalne.
Dane wyjsciowe: Lista zawierajaca liczby naturalne.
Przyklad:
Dla wejsciowej listy:
[[ -6, 23, 29, 33],
[ 6, 22, 35, 71 ],
[ 5, 19, 21, 37 ],
[ -12, -7, -3, 28 ]],
powinna zostac zwrocona lista: [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71].

"""

import heapq

class Node(object):
    def __init__(self, wartosc: int, i: int, indeks: int):
        self.wartosc = wartosc
        self.i = i
        self.indeks = indeks

    def __lt__(self, inny):
        return self.wartosc < inny.wartosc

# Zlozonosc czasowa: O(nlogm)
# Zalozenie pop/push O(logm)
def polacz_listy_v1(lista):

    M = len(lista)

    sterta = [Node(lista[i][0], i, 0) for i in range(M) if len(lista[i]) >= 1]
    heapq.heapify(sterta)
    wynik = []

    while len(heap) > 0:

        min = heapq.heappop(sterta)
        wynik.append(min.wartosc)

        if min.indeks + 1 < len(lista[min.i]):
            min.indeks += 1
            min.wartosc = lista[min.i][min.indeks]
            heapq.heappush(sterta, min)

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

