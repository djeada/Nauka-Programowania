"""
Dla pobranych sześciu liczb: dnia urodzenia osoby, miesiąca urodzenia osoby, 
roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiąca i aktualnego 
roku, sprawdź czy dana osoba jest pełnoletnia.
"""

if __name__ == "__main__":

    print("Podaj datę urodzenia osoby (dzien, miesiac, rok):")
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
        print("Osoba jest pełnoletnia.")

    elif roznica_lat == 18:

        if roznica_miesiecy > 0:
            print("Osoba jest pełnoletnia.")

        elif roznica_miesiecy == 0:

            if roznica_dni >= 0:
                print("Osoba jest pełnoletnia.")

            else:
                print("Osoba nie jest pełnoletnia.")
        else:
            print("Osoba nie jest pełnoletnia.")
    else:
        print("Osoba nie jest pełnoletnia.")
        
