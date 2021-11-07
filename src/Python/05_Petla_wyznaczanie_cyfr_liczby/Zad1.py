"""
Dla pobranej od uzytkownika, wypisz liczbe cyfr pobranej liczby.
"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    cyfry = 0
    while liczba > 0:
        cyfry += 1
        liczba //= 10

    print("Liczba cyfr: ", cyfry)
