"""
Wypisz na przemian elemnty pierwszej i drugiej listy. 
Warunek: listy majac byc rownej dlugosci.
Wynik: jedna lista skladajaca sie z elementow obu otrzymanych list.
"""

# Wersja 1
def polacz_listy_v1(list_a, lista_b):

    if len(list_a) != len(lista_b):
        return False

    wynik = []

    for i in range(len(lista_a)):
        wynik.append(lista_a[i])
        wynik.append(lista_b[i])

    return wynik


# Wersja 2
def polacz_listy_v2(list_a, lista_b):

    if len(list_a) != len(lista_b):
        return False

    wynik = []

    for a, b in zip(lista_a, lista_b):
        wynik.append(a)
        wynik.append(b)

    return wynik


# Testy Poprawnosci
lista_a = ["a", "c", "e"]
lista_b = ["b", "d", "f"]
wynik = ["a", "b", "c", "d", "e", "f"]

assert polacz_listy_v1(lista_a, lista_b) == wynik
assert polacz_listy_v2(lista_a, lista_b) == wynik
