"""
Tytul: Suma liczb mniejszych od podanej.
Tresc: Dla otrzymanej liczby naturalnej wypisz sume wszystkich liczb naturalnych mniejszych od niej.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba.
Przyklad:
Dla otrzymanej liczby 5, powinna zostac wypisana liczba 10.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    suma = 0
    for i in range(1, liczba):
        suma += i

    print("Suma wszystkich liczb mniejszych od podanej liczby wynosi: ", suma)
