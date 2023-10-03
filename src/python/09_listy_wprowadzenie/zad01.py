"""
Tytul: Wczytaj i wypisz.
Tresc: Dla podanej liczby naturalnej N, wczytaj N liczb calkowitych do listy, a nastepnie:
a) Wypisz liste od poczatku do konca, z kazdym elementem w osobnym wierszu.
b) Wypisz liste od konca, z elementami oddzielonymi przecinkami i wypisanymi w jednym wierszu.
Dane wejsciowe: N liczb calkowitych.
Dane wyjsciowe: N liczb.
Przyklad:
Dla N rownego 3 oraz pobranych liczb: 8, 12, 7, w drugim podpunkcie powinno zostac wypisane: 7, 12, 8.

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
