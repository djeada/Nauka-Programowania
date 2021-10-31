"""
Dla pobranej od użytkownika, wypisz liczbę cyfr pobranej liczby.
"""

if __name__ == "__main__":

    print("Podaj liczbę: ")
    liczba = int(input())

    cyfry = 0
    while liczba > 0:
        cyfry += 1
        liczba //= 10

    print("Liczba cyfr: ", cyfry)
