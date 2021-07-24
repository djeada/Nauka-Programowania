"""
Znajdz takie pary elementow w liscie, ktorych suma jest rowna liczbie.
Element nie moze byc w parze sam ze soba.
"""

# Wersja 1
# Zlozonosc czasowa O(n^2)
# Zlozonosc pamieciowa O(1)
def znajdz_pary_v1(lista, liczba):

    wynik = []

    for i in range(len(lista) - 1):

        for j in range(i + 1, len(lista)):

            if lista[i] + lista[j] == liczba:
                wynik.append((lista[i], lista[j]))

    return wynik


# Wersja 2
# Zlozonosc czasowa O(nlogn)
# Zlozonosc pamieciowa O(1)
def znajdz_pary_v2(lista, liczba):

    wynik = []
    lista.sort()

    l, p = 0, (len(lista) - 1)

    while l < p:

        if lista[l] + lista[p] == liczba:
            wynik.append((lista[l], lista[p]))

            if l + 1 < p and lista[l + 1] == lista[l]:
                if lista[l + 1] + lista[l] == liczba:
                    wynik.append((lista[l], lista[l + 1]))
                l += 1

            else:
                p -= 1

        else:
            if lista[l] + lista[p] < liczba:
                l += 1

            else:
                p -= 1

    return wynik


# Wersja 3
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(n)
def znajdz_pary_v3(lista, liczba):

    wynik = []
    histo = {}

    for x in lista:
        if x in histo:
            histo[x] += 1
        else:
            histo[x] = 1

    for x in lista:
        if (
            liczba - x in histo
            and (x, liczba - x) not in wynik
            and (liczba - x, x) not in wynik
        ):

            if liczba - x != x:
                for i in range(histo[x] * histo[liczba - x]):
                    wynik.append((x, liczba - x))

            else:
                for i in range(histo[x]):
                    wynik.append((x, liczba - x))

    return wynik


# Testy Poprawnosci
lista = [0, 4, 5, 6, 2, 9, 2, 3]
liczba = 5
wynik = [(0, 5), (2, 3), (2, 3)]

assert sorted(znajdz_pary_v1(lista, liczba)) == sorted(wynik)
assert sorted(znajdz_pary_v2(lista, liczba)) == sorted(wynik)
assert sorted(znajdz_pary_v3(lista, liczba)) == sorted(wynik)

lista = [3, 3, 3]
liczba = 6
wynik = [(3, 3), (3, 3), (3, 3)]

assert sorted(znajdz_pary_v1(lista, liczba)) == sorted(wynik)
assert sorted(znajdz_pary_v2(lista, liczba)) == sorted(wynik)
assert sorted(znajdz_pary_v3(lista, liczba)) == sorted(wynik)
