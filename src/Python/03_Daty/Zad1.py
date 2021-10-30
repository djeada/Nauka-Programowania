"""
Wypisz pobraną od użytkownika liczbę, jeśli:

a) Liczba jest poprawnym numerem dnia tygodnia.
b) Liczba jest poprawnym numerem miesiąca.
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
