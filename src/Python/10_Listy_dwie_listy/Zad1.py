"""
Dla otrzymanych dwoch list wypisuj na przemian elementy pierwszej 
i drugiej listy. Jesli listy nie sa rownej dlugosci po wyczerpaniu 
elementow krotszej listy, wypisuj tylko elementy dluzszej listy.
"""


def wypisz_na_przemian(lista_a, lista_b):

    min_dlugosc = min(len(lista_a), len(lista_b))

    for i in range(min_dlugosc):
        print(f"{lista_a[i]}, {lista_b[i]}", end=", ")

    for i in range(min_dlugosc, len(lista_a)):
        print(f"{lista_a[i]}, 0", end=", ")

    for i in range(min_dlugosc, len(lista_b)):
        print(f"0, {lista_b[i]}", end=", ")

    print()


if __name__ == "__main__":

    print("Podaj dlugosc pierwszej listy")
    dlugosc_a = int(input())

    print(f"Podaj {dlugosc_a} elementow:")
    lista_a = [int(input()) for i in range(dlugosc_a)]

    print("Podaj dlugosc drugiej listy")
    dlugosc_b = int(input())

    print(f"Podaj {dlugosc_b} elementow:")
    lista_b = [int(input()) for i in range(dlugosc_b)]

    wypisz_na_przemian(lista_a, lista_b)
