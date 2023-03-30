"""
Tytul: Porownanie ze stala.
Tresc: Pobierz od uzytkownika liczbe naturalna. Jesli ta liczba jest wieksza niz 5, wypisz ja.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna lub brak danych wyjsciowych.
Przyklad:
Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.

"""

if __name__ == "__main__":

    print("podaj liczbe:")

    x = int(input())

    if x > 5:
        print(x)

