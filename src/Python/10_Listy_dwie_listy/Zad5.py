"""
Znajdź część wspólną dwóch list.
"""

# Wersja 1
def czesc_wspolna_v1(lista_a, lista_b):
    wynik = []
    for x in lista_a:
        if x in lista_b:
            wynik.append(x)
    return wynik


# Wersja 2
# Z uzyciem zbiorow, tylko dla list z unikalnymi elementami!
def czesc_wspolna_v2(lista_a, lista_b):
    return set(lista_a) - (set(lista_a) - set(lista_b))


# Testy Poprawnosci
lista_a = [3, 6, 2, 7, 9]
lista_b = [4, 2, 3, 5, 6]
wynik = [3, 6, 2]

assert sorted(czesc_wspolna_v1(lista_a, lista_b)) == sorted(wynik)
assert sorted(czesc_wspolna_v2(lista_a, lista_b)) == sorted(wynik)

lista_a = [61, 96, 25, 46, 84, 29, 48, 87, 53, 92, 71]
lista_b = [71, 9, 25, 96, 74, 39, 13, 84]
wynik = [25, 71, 84, 96]

assert sorted(czesc_wspolna_v1(lista_a, lista_b)) == sorted(wynik)
assert sorted(czesc_wspolna_v2(lista_a, lista_b)) == sorted(wynik)
