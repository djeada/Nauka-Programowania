"""

Wypisz pobrana od uzytkownika liczbe, jesli:
a) jest poprawnym numerem tygodnia.
b) jest poprawnym numerem miesiaca.

"""

print("podaj numer dnia tygodnia i numer miesiaca")

a = int(input())
b = int(input())

if a >= 1 and a <= 7:

    print("liczba dni jest poprawna")
else:
    print("liczba dni jest nie poprawna")

if b >= 1 and b <= 12:
    print("liczba miesiecy jest poprawna")
else:
    print("liczba miesiecy jest nie poprawna")
