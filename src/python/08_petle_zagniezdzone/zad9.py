import math

"""
Napisz funkcje, ktora dla otrzymanej liczby N, 
wypisze N pierwszych liczb pierwszych.
"""


def sito_eratostenesa(n):
    tablica = [True] * n
    tablica[0] = False
    tablica[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if tablica[i]:
            for j in range(i ** 2, n, i):
                tablica[j] = False
    return tablica


if __name__ == "__main__":

    print("Podaj liczbe n:")
    n = int(input())

    tablica = sito_eratostenesa(n)
    for i in range(len(tablica)):
        if tablica[i]:
            print(f"{i}, ", end="")

    print()
