import unittest
import time
import random

"""
Polacz posortowane listy w posortowana liste.
"""

# Wersja 1
def polaczPosortowaneListyV1(listaA, listaB):

    if not listaA:
        return list(listaB)

    if not listaB:
        return list(listaA)

    listaC = []

    i = 0
    j = 0

    while i < len(listaA) and j < len(listaB):
        if listaA[i] < listaB[j]:
            listaC.append(listaA[i])
            i += 1
        else:
            listaC.append(listaB[j])
            j += 1

    for k in range(i, len(listaA)):
        listaC.append(listaA[k])

    for k in range(j, len(listaB)):
        listaC.append(listaB[k])

    return listaC


# Wersja 2
def polaczPosortowaneListyV2(listaA, listaB):

    if not listaA:
        return list(listaB)

    if not listaB:
        return list(listaA)

    listaC = []

    if listaA[-1] > listaB[-1]:
        listaA, listaB = listaB, listaA

    it = iter(listaB)
    elementListyB = it.__next__()
    listaC = []

    for elementListyA in listaA:
        try:
            while listaB and elementListyB < elementListyA:
                listaC.append(elementListyB)
                elementListyB = it.__next__()
        except StopIteration:
            break
        listaC.append(elementListyA)

    listaC.append(elementListyB)
    listaC.extend(it)

    return listaC


# Wersja 3
def polaczPosortowaneListyV3(listaA, listaB):
    if not listaA:
        return list(listaB)

    if not listaB:
        return list(listaA)

    return sorted(listaA + listaB)


# Testy Poprawnosci
a = [5, 7, 11]
b = [1, 3, 8, 14]
c = [1, 3, 5, 7, 8, 11, 14]

assert polaczPosortowaneListyV1(a, b) == c
assert polaczPosortowaneListyV2(a, b) == c
assert polaczPosortowaneListyV3(a, b) == c

# Testy Predkosci
def zmierzCzas(n, f):

    a = [random.random() for i in range(n)]
    b = [random.random() for i in range(n)]

    start = time.time()
    f(a, b)
    end = time.time()

    return end - start


listaFunkcji = [
    polaczPosortowaneListyV1,
    polaczPosortowaneListyV2,
    polaczPosortowaneListyV3,
]

for f in listaFunkcji:
    print([zmierzCzas(10, f), zmierzCzas(10 ** 3, f), zmierzCzas(10 ** 6, f)])
