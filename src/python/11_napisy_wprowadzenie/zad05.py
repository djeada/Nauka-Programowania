"""
Tytul: Wypisz co k-ty znak napisu poziomo i pionowo.
Tresc: Otrzymasz napis oraz liczbe k.
a) Wypisz co k-ty znak napisu poziomo, rozdzielajac znaki spacjami.
b) Wypisz co k-ty znak napisu pionowo, rozdzielajac znaki enterami.
Dane wejsciowe: Napis oraz liczba.
Dane wyjsciowe: Napis.
Przyklad:
a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis: "z h n".
b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis:
z
h
n

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
