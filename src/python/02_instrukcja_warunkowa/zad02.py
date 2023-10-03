"""
Tytul: Porownanie ze zmienna.
Tresc: Pobierz od uzytkownika dwie liczby naturalne i sprawdz, czy sa one identyczne. Wypisz odpowiedni komunikat.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla pobranych liczb: 7 i 4, powinien zostac wypisany komunikat, ze liczby sa rozne.

"""

if __name__ == "__main__":

    print("podaj dwie liczby")

    a = int(input())
    b = int(input())

    if a == b:
        print("liczby sa jednakowe")
    else:
        print("liczby sa rozne")
