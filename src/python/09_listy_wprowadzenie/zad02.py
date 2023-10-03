"""
Tytul: Wczytaj, zmodyfikuj i wypisz.
Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie. Nastepnie:
a) Dodaj 1 do kazdego elementu listy.
b) Pomnoz kazdy element przez jego indeks w liscie (indeksy zaczynaja sie od 0).
c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.
Dla kazdego z powyzszych podpunktow wypisz zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
Dane wejsciowe: N oraz N liczb calkowitych.
Dane wyjsciowe: N liczb calkowitych.
Przyklad:
Dla N rownego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.

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
