"""
Dla pobranej liczby, wypisz dzien tygodnia odpowiadajacy tej liczbie. 
Jesli otrzymano liczbe niedodatnia, badz dodatnia wieksza niz 7, 
wypisz komuniat informujacy uzytkownika, ze liczba jest niepoprawna.
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
