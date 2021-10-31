"""
Dla pobranej od użytkownika liczby, wypisz wszystkie liczby naturalne:

a) Mniejsze od pobranej liczby, których suma cyfr jest równa 10.
b) Dwucyfrowe, większe od pobranej liczby.
c) Trzycyfrowe, których suma cyfr jest równa pobranej liczbie.
d) Trzycyfrowe podzielne przez sumę cyfr pobranej liczby.
e) Mniejsze od pobranej liczby, składające się wyłącznie z parzystych cyfr.
"""

if __name__ == "__main__":
    print("Podaj liczbę: ")
    liczba = int(input())

    print("Liczby mniejsze od pobranej liczby, których suma cyfr jest równa 10: ")

    for i in range(1, liczba):
        suma = 0
        for j in str(i):
            suma += int(j)
        if suma == 10:
            print(i)

    print("Liczby dwucyfrowe, większe od pobranej liczby: ")

    for i in range(liczba + 1, 100):
        print(i)

    print("Liczby trzycyfrowe, których suma cyfr jest równa pobranej liczbie: ")

    for i in range(100, 1000):
        suma = 0
        kopia = i
        while kopia > 0:
            suma += kopia % 10
            kopia //= 10
        if suma == liczba:
            print(i)

    print("Liczby trzycyfrowe podzielne przez sumę cyfr pobranej liczby: ")

    suma = 0
    kopia = liczba
    while kopia > 0:
        suma += kopia % 10
        kopia //= 10

    for i in range(100, 1000):
        if i % suma == 0:
            print(i)

    print(
        "Liczby mniejsze od pobranej liczby, składające się wyłącznie z parzystych cyfr: "
    )

    for i in range(1, liczba):
        flaga = True
        kopia = i
        while kopia > 0:
            if kopia % 2 == 0:
                kopia //= 10
            else:
                flaga = False
                break
        if flaga:
            print(i)
