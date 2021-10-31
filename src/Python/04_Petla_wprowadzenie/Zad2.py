"""
Dla pobranej liczby, powinny zostać wypisane wszystkie 
liczby naturalne mniejsze od podanej liczby.
"""

if __name__ == "__main__":

    print("Podaj liczbę: ")
    liczba = int(input())

    for i in range(1, liczba):
        print(i)
