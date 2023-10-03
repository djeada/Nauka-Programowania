"""
Tytul: Liczby mniejsze od podanej liczby.
Tresc: Dla otrzymanej liczby naturalnej wypisz wszystkie liczby naturalne mniejsze od niej.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczby naturalne.
Przyklad:
Dla otrzymanej liczby 3, powinny zostac wypisane liczby 2 i 1.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    for i in range(1, liczba):
        print(i)
