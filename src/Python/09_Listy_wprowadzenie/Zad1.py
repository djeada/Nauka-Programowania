"""
Dla liczby N, wczytaj N liczb do listy, a następnie:

a) Wypisz listę od początku do końca. Elementy listy 
powinny znajdować się w osobnych wierszach.
b) Wypisz listę od końca. Elementy listy powinny być 
oddzielone przecinkami i wypisane w jednym wierszu.
"""


def wypisz_od_poczatku(lista):
    for element in lista:
        print(element)


def wypisz_od_konca(lista):
    for element in reversed(lista):
        print(f"{element}, ", end=", ")
    print()


if __name__ == "__main__":

    print("Podaj liczbe elementow listy: ", end="")
    n = int(input())

    lista = []
    for i in range(n):
        print(f"Podaj element {i+1} listy: ", end="")
        lista.append(int(input()))

    print("\nLista od poczatku: ")
    wypisz_od_poczatku(lista)

    print("\nLista od konca: ")
    wypisz_od_konca(lista)
