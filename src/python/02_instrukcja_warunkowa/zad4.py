"""
Tytul: Maksimum i minimum z dwoch liczb.
Tresc: Pobierz od uzytkownika dwie liczby naturalne i wypisz najpierw wieksza, a potem mniejsza.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla pobranych liczb: 1 oraz 4, powinny zostac wypisane liczby: 4 i 1.

"""

if __name__ == "__main__":

    print("podaj dwie liczby")

    a = int(input())
    b = int(input())

    if a < b:
        print(b)
        print(a)
        print(" druga liczba jest wieksza od pierwszej")
    else:
        print(a)
        print(b)
        print("druga liczba nie jest wieksza od pierwszej")

