"""
Tytul: Liczba cyfr.
Tresc: Dla otrzymanej od uzytkownika liczby naturalnej wypisz liczbe cyfr, z ktorych sie sklada.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 342, powinna zostac wypisana liczba 3.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    cyfry = 0
    while liczba > 0:
        cyfry += 1
        liczba //= 10

    print("Liczba cyfr: ", cyfry)

