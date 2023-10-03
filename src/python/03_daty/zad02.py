"""
Tytul: Czy osoba jest pelnoletnia?
Tresc: Dla pobranych szesciu liczb: dnia urodzenia osoby, miesiaca urodzenia osoby, roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiaca i aktualnego roku, sprawdz czy dana osoba jest pelnoletnia.
Dane wejsciowe: 6 liczb.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla pobranych liczb: 5, 12, 1999, 20, 11, 2020, powinna zostac wypisana informacja o pelnoletnosci osoby.

"""

if __name__ == "__main__":

    print("Podaj date urodzenia osoby (dzien, miesiac, rok):")
    dzien_urodzenia = int(input())
    miesiac_urodzenia = int(input())
    rok_urodzenia = int(input())

    print("Podaj aktualna date (dzien, miesiac, rok):")
    aktualny_dzien = int(input())
    aktualny_miesiac = int(input())
    aktualny_rok = int(input())

    roznica_lat = aktualny_rok - rok_urodzenia
    roznica_miesiecy = aktualny_miesiac - miesiac_urodzenia
    roznica_dni = aktualny_dzien - dzien_urodzenia

    if roznica_lat > 18:
        print("Osoba jest pelnoletnia.")

    elif roznica_lat == 18:

        if roznica_miesiecy > 0:
            print("Osoba jest pelnoletnia.")

        elif roznica_miesiecy == 0:

            if roznica_dni >= 0:
                print("Osoba jest pelnoletnia.")

            else:
                print("Osoba nie jest pelnoletnia.")
        else:
            print("Osoba nie jest pelnoletnia.")
    else:
        print("Osoba nie jest pelnoletnia.")
