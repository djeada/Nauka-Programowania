"""
Tytul: Ile dni ma miesiac?
Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal liczbe dni w miesiacu odpowiadajacemu tej liczbie. Jesli pobrana liczba nie jest poprawnym numerem miesiaca, program powinien poinformowac o tym uzytkownika.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla pobranej liczby 1, program powinien zwrocic liczbe 31.

"""

if __name__ == "__main__":

    print("Podaj numer miesiaca:")
    miesiac = int(input())

    if miesiac == 1:
        print("Styczen ma 31 dni.")
    elif miesiac == 2:
        print("Luty ma 28 lub 29 dni.")
    elif miesiac == 3:
        print("Marzec ma 31 dni.")
    elif miesiac == 4:
        print("Kwiecien ma 30 dni.")
    elif miesiac == 5:
        print("Maj ma 31 dni.")
    elif miesiac == 6:
        print("Czerwiec ma 30 dni.")
    elif miesiac == 7:
        print("Lipiec ma 31 dni.")
    elif miesiac == 8:
        print("Sierpien ma 31 dni.")
    elif miesiac == 9:
        print("Wrzesien ma 30 dni.")
    elif miesiac == 10:
        print("Pazdziernik ma 31 dni.")
    elif miesiac == 11:
        print("Listopad ma 30 dni.")
    elif miesiac == 12:
        print("Grudzien ma 31 dni.")
    else:
        print("Niepoprawny numer miesiaca.")

