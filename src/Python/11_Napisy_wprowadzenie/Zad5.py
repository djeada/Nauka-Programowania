"""
Otrzymujesz napis oraz liczbe k. 
a) Wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
b) Wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.
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
