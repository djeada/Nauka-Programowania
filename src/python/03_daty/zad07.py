"""
Tytul: Ile dni minelo od poczatku roku?
Tresc: Dla trzech pobranych liczb: reprezentujacych date wypisz, ile dni minelo od poczatku roku. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostac zwrocona liczba 45. **

"""

if __name__ == "__main__":

    print("Podaj date:")
    dzien = int(input())
    miesiac = int(input())
    rok = int(input())

    liczba_dni = 0

    if miesiac == 1:
        liczba_dni = dzien
    elif miesiac == 2:
        liczba_dni = 31 + dzien
    elif miesiac == 3:
        liczba_dni = 59 + dzien
    elif miesiac == 4:
        liczba_dni = 90 + dzien
    elif miesiac == 5:
        liczba_dni = 120 + dzien
    elif miesiac == 6:
        liczba_dni = 151 + dzien
    elif miesiac == 7:
        liczba_dni = 181 + dzien
    elif miesiac == 8:
        liczba_dni = 212 + dzien
    elif miesiac == 9:
        liczba_dni = 243 + dzien
    elif miesiac == 10:
        liczba_dni = 273 + dzien
    elif miesiac == 11:
        liczba_dni = 304 + dzien
    elif miesiac == 12:
        liczba_dni = 334 + dzien
    else:
        print("Niepoprawny miesiac")

    if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
        if miesiac > 2:
            liczba_dni += 1

    print(f"Od poczatku roku uplynelo: {liczba_dni}")

