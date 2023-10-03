"""
Tytul: Znak liczby.
Tresc: Pobierz liczbe naturalna od uzytkownika i sprawdz, czy liczba jest ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla pobranej liczby: 2, powinien zostac wypisany komunikat, ze liczba jest dodatnia.

"""

if __name__ == "__main__":
    print("podaj liczbe")

    a = int(input())

    if a < 0:
        print("libczba jest ujemna")
    elif a > 0:
        print("liczba jest dodatnia")
    else:
        print("liczba jest zerem")
