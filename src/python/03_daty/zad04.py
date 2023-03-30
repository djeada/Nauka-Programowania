"""
Tytul: Dzien tygodnia odpowiadajacy danej liczbie.
Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal dzien tygodnia odpowiadajacy tej liczbie. Jesli otrzymano liczbe niedodatnia badz dodatnia wieksza niz 7, program powinien wypisac komunikat informujacy uzytkownika, ze liczba jest niepoprawna.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat o dniu tygodnia.
Przyklad:
Dla pobranej liczby 2, program powinien wypisac napis "Wtorek".

"""

if __name__ == "__main__":

    print("Podaj liczbe:")
    liczba = int(input())

    if liczba < 0 or liczba > 7:
        print("Liczba niepoprawna")
    elif liczba == 1:
        print("Pierwszym dniem tygodnia jest poniedzialek.")
    elif liczba == 2:
        print("Drugim dniem tygodnia jest wtorek.")
    elif liczba == 3:
        print("Trzecim dniem tygodnia jest sroda.")
    elif liczba == 4:
        print("Czwartym dniem tygodnia jest czwartek.")
    elif liczba == 5:
        print("Piatym dniem tygodnia jest piatek.")
    elif liczba == 6:
        print("Szostym dniem tygodnia jest sobota.")
    elif liczba == 7:
        print("Siodmym dniem tygodnia jest niedziela.")

