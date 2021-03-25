"""
Znajdź część wspólną dwóch list.
"""

# Wersja 1
def czescWspolnaV1(listaA, listaB):
    wynik = []
    for x in listaA:
        if x in listaB:
            wynik.append(x)
    return wynik


# Wersja 2
# Z uzyciem zbiorow, tylko dla list z unikalnymi elementami!
def czescWspolnaV2(listaA, listaB):
    return set(listaA) - (set(listaA) - set(listaB))


# Testy Poprawnosci
listaA = [3, 6, 2, 7, 9]
listaB = [4, 2, 3, 5, 6]
wynik = [3, 6, 2]

assert sorted(czescWspolnaV1(listaA, listaB)) == sorted(wynik)
assert sorted(czescWspolnaV2(listaA, listaB)) == sorted(wynik)

listaA = [61, 96, 25, 46, 84, 29, 48, 87, 53, 92, 71]
listaB = [71, 9, 25, 96, 74, 39, 13, 84]
wynik = [25, 71, 84, 96]

assert sorted(czescWspolnaV1(listaA, listaB)) == sorted(wynik)
assert sorted(czescWspolnaV2(listaA, listaB)) == sorted(wynik)
