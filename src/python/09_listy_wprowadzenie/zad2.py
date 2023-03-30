"""
Tytul: Samochody jadace w przeciwnych kierunkach.
Tresc: Otrzymujesz liste zlozona wylacznie z liter 'A' i 'B', ktore odpowiadaja samochodom jadacym odpowiednio na wschod ('A') i zachod ('B'). Policz, ile razy samochody jadace w przeciwnych kierunkach mijaja sie.
Dane wejsciowe: Lista znakow odpowiadajacych samochodom jadacym na wschod ('A') i zachod ('B').
Dane wyjsciowe: Liczba naturalna oznaczajaca liczbe mijajacych sie samochodow.
Przyklad:
Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostac zwrocona liczba 5.

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

