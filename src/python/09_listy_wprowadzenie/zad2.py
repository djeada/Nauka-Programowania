"""
Dla liczby N, wczytaj N liczb do listy, a nastepnie:

a) Dodaj 1 do kazdego elementu.
b) Pomnoz kazdy element przez jego indeks.
c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.

Dla kazdego podpunktu wypisz zmodyfikowana liste. Elementy listy 
powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
"""


def dodaj_1(lista):
    return [element + 1 for element in lista]


def pomnoz_przez_indeks(lista):
    return [element * indeks for indeks, element in enumerate(lista)]


def zastap_pierwszym(lista):
    return [lista[0] for element in lista]


if __name__ == "__main__":

    print("Podaj liczbe elementow listy: ")
    n = int(input())

    lista = []
    for i in range(n):
        print(f"Podaj element {i+1} listy: ", end="")
        lista.append(int(input()))

    print(f"Lista przed modyfikacja: {lista}")

    print(f"Lista po dodaniu 1 do kazdego elementu: {dodaj_1(lista)}")
    print(
        f"Lista po pomnozeniu kazdego elementu przez indeks: {pomnoz_przez_indeks(lista)}"
    )
    print(
        f"Lista po zastapieniu kazdego elementu wartoscia pierwszego elementu: {zastap_pierwszym(lista)}"
    )
