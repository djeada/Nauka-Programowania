"""
Tytul: Napis skladajacy sie z liczb od 1 do n.
Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb naturalnych od 1 do n.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".

"""

def wypisz_poziomo(napis, k):
    for i in range(len(napis)):
        if i % k == 0:
            print(napis[i], end=" ")
    print()

def wypisz_pionowo(napis, k):
    for i in range(len(napis)):
        if i % k == 0:
            print(napis[i])

if __name__ == "__main__":

    napis = input("Podaj napis: ")
    k = int(input("Podaj liczbe k: "))

    print("Napis wypisany poziomo: ")
    wypisz_poziomo(napis, k)

    print("Napis wypisany pionowo: ")
    wypisz_pionowo(napis, k)

