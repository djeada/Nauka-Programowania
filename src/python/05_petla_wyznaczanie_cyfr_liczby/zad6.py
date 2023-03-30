"""
Tytul: Liczby spelniajace okreslone warunki.
Tresc: Dla pobranej liczby naturalnej wypisz:
a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10,
b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej,
c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie,
d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby,
e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr.
Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
Dane wyjsciowe: Kilka liczb naturalnych.
Przyklady
Dla pobranej liczby: 95:
a) wszystkie liczby naturalne mniejsze od pobranej, ktorych suma cyfr jest rowna 10: brak
b) wszystkie liczby naturalne dwucyfrowe wieksze od pobranej: 96, 97, 98, 99
c) wszystkie liczby naturalne trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie: brak
d) wszystkie liczby naturalne trzycyfrowe podzielne przez sume cyfr pobranej liczby: brak
e) wszystkie liczby naturalne mniejsze od pobranej, skladajace sie wylacznie z parzystych cyfr: 2, 4

"""

if __name__ == "__main__":
    print("Podaj liczbe: ")
    liczba = int(input())

    print("Liczby mniejsze od pobranej liczby, ktorych suma cyfr jest rowna 10: ")

    for i in range(1, liczba):
        suma = 0
        for j in str(i):
            suma += int(j)
        if suma == 10:
            print(i)

    print("Liczby dwucyfrowe, wieksze od pobranej liczby: ")

    for i in range(liczba + 1, 100):
        print(i)

    print("Liczby trzycyfrowe, ktorych suma cyfr jest rowna pobranej liczbie: ")

    for i in range(100, 1000):
        suma = 0
        kopia = i
        while kopia > 0:
            suma += kopia % 10
            kopia //= 10
        if suma == liczba:
            print(i)

    print("Liczby trzycyfrowe podzielne przez sume cyfr pobranej liczby: ")

    suma = 0
    kopia = liczba
    while kopia > 0:
        suma += kopia % 10
        kopia //= 10

    for i in range(100, 1000):
        if i % suma == 0:
            print(i)

    print(
        "Liczby mniejsze od pobranej liczby, skladajace sie wylacznie z parzystych cyfr: "
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

