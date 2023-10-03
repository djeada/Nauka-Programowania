"""
Tytul: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiaca?
Tresc: Wypisz pobrana od uzytkownika liczbe naturalna, jesli jest ona poprawnym numerem dnia tygodnia lub miesiaca.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
* Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.
* Dla pobranej liczby: 15, nie powinna byc wypisana zadna liczba.

"""

if __name__ == "__main__":

    print("Podaj liczbe:")

    a = int(input())
    b = int(input())

    if a >= 1 and a <= 7:
        print("Liczba jest poprawnym numerem tygodnia.")
    else:
        print("Liczba nie jest poprawnym numerem tygodnia.")

    if b >= 1 and b <= 12:
        print("Liczba jest poprawnym numerem miesiaca.")
    else:
        print("Liczba nie jest poprawnym numerem miesiaca.")
