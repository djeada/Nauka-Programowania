"""
Tytul: Posortowanie trzech liczb.
Tresc: Pobierz od uzytkownika trzy liczby naturalne i wypisz je w kolejnosci rosnacej.
Dane wejsciowe: Trzy liczby naturalne.
Dane wyjsciowe: Trzy liczby naturalne.
Przyklad:
Dla pobranych liczb: 2, 1 oraz 4, powinny zostac wypisane liczby: 1, 2 i 4.

"""

if __name__ == "__main__":

    print("podaj trzy liczby")

    a = int(input())
    b = int(input())
    c = int(input())

    if a >= b and a >= c:
        if b >= c:
            print(c, b, a)
        else:
            print(b, c, a)

    elif c >= b and c >= a:
        if a >= b:
            print(b, a, c)
        else:
            print(a, b, c)

    else:
        if a >= c:
            print(c, a, b)
        else:
            print(a, c, b)

