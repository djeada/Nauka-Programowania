"""
Dla pobranej liczby, powinna zostać wypisana suma cyfr tej liczby.
"""

if __name__ == "__main__":

    liczba = int(input("Podaj liczbę: "))

    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10

    print(f"Suma cyfr wynosi: {suma}")
