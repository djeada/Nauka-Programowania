"""
Tytul: Wypisanie elementow dwoch list na przemian.
Tresc: Dla otrzymanych dwoch list, wypisuj na przemian elementy z obu list. Jesli listy nie sa tej samej dlugosci, po wyczerpaniu elementow krotszej listy, wypisuj pozostale elementy dluzszej listy.
Dane wejsciowe: Dwie listy.
Dane wyjsciowe: Kilka liczb.
Przyklad:
Dla otrzymanych list [5, 3, 7, 2] oraz [1, -2, 3], zostana wypisane: 5, 1, 3, -2, 7, 3, 2.

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
