"""
Dla pobranej liczby, powinna zostać wypisana suma 
wszystkich liczb naturalnych mniejszych od pobranej liczby.
"""

if __name__ == "__main__":

    print("Podaj liczbę: ")
    liczba = int(input())

    suma = 0
    for i in range(1, liczba):
        suma += i
    
    print("Suma wszystkich liczb mniejszych od podanej liczby wynosi: ", suma)