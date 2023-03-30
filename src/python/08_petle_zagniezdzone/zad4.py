"""
Tytul: Tabliczka mnozenia.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N pierwszych wierszy i kolumn tabliczki mnozenia.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Wiersze i kolumny tabliczki mnozenia o wymiarach NxN.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
1 2 3
2 4 6
3 6 9

"""

def tabliczka_mnozenia(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end=" ")
        print()

if __name__ == "__main__":

    print("Podaj liczbe: ")
    n = int(input())

    tabliczka_mnozenia(n)

