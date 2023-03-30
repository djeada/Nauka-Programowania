"""
Tytul: Maks z czterech liczb.
Tresc: Dla czterech pobranych liczb naturalnych, wypisz najwieksza z nich.
Dane wejsciowe: Cztery liczby naturalne.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla pobranych liczb: 2, 5, 1 i 4, powinna zostac wypisana liczba: 5.

"""

if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    maks_ab = a if a > b else b

    maks_cd = c if c > d else d

    maks = maks_ab if maks_ab > maks_cd else maks_cd

    print(maks)

