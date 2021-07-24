import unittest
import time
import random

"""
Polacz posortowane listy w posortowana liste.
"""

# Wersja 1
def polacz_posortowane_listy_v1(lista_a, lista_b):

    if not lista_a:
        return list(lista_b)

    if not lista_b:
        return list(lista_a)

    lista_c = []

    i = 0
    j = 0

    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] < lista_b[j]:
            lista_c.append(lista_a[i])
            i += 1
        else:
            lista_c.append(lista_b[j])
            j += 1

    for k in range(i, len(lista_a)):
        lista_c.append(lista_a[k])

    for k in range(j, len(lista_b)):
        lista_c.append(lista_b[k])

    return lista_c


# Wersja 2
def polacz_posortowane_listy_v2(lista_a, lista_b):

    if not lista_a:
        return list(lista_b)

    if not lista_b:
        return list(lista_a)

    lista_c = []

    if lista_a[-1] > lista_b[-1]:
        lista_a, lista_b = lista_b, lista_a

    it = iter(lista_b)
    element_listy_b = it.__next__()
    lista_c = []

    for element_listy_a in lista_a:
        try:
            while lista_b and element_listy_b < element_listy_a:
                lista_c.append(element_listy_b)
                element_listy_b = it.__next__()
        except StopIteration:
            break
        lista_c.append(element_listy_a)

    lista_c.append(element_listy_b)
    lista_c.extend(it)

    return lista_c


# Wersja 3
def polacz_posortowane_listy_v3(lista_a, lista_b):
    if not lista_a:
        return list(lista_b)

    if not lista_b:
        return list(lista_a)

    return sorted(lista_a + lista_b)


# Testy Poprawnosci
a = [5, 7, 11]
b = [1, 3, 8, 14]
c = [1, 3, 5, 7, 8, 11, 14]

assert polacz_posortowane_listy_v1(a, b) == c
assert polacz_posortowane_listy_v2(a, b) == c
assert polacz_posortowane_listy_v3(a, b) == c

# Testy Predkosci
def zmierz_czas(n, f):

    a = [random.random() for i in range(n)]
    b = [random.random() for i in range(n)]

    start = time.time()
    f(a, b)
    end = time.time()

    return end - start


lista_funkcji = [
    polacz_posortowane_listy_v1,
    polacz_posortowane_listy_v2,
    polacz_posortowane_listy_v3,
]

for f in lista_funkcji:
    print([zmierz_czas(10, f), zmierz_czas(10 ** 3, f), zmierz_czas(10 ** 6, f)])
