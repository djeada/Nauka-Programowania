"""
Dla pobranej liczby n, wypisz sumę n pierwszych wyrazów ciągu danego wzorem:

a) a_n = n/(n + 1)
b) a_n = (n^2 + 5)/n
c) a_n = n + 2^n

Wynik powinien być zaokrąglony do najbliższej liczby naturalnej.
"""

if __name__ == "__main__":

    print("Podaj liczbę n: ")
    n = int(input())

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = n/(n + 1) wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += i / (i + 1)

    print(suma)

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = (n^2 + 5)/n wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += (i ** 2 + 5) / i

    print(suma)

    print("Suma n pierwszych wyrazow ciagu danego wzorem a_n = n + 2^n wynosi:")
    suma = 0
    for i in range(1, n + 1):
        suma += i + 2 ** i

    print(suma)
