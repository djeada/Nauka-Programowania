"""
Tytul: Srednia z n liczb
Tresc: Napisz funkcje, ktora dla otrzymanej liczby n, poprosi uzytkownika o podanie n liczb i zwroci ich srednia arytmetyczna.
Dane wejsciowe: liczba naturalna n oraz n liczb
Dane wyjsciowe: liczba naturalna
Przyklad:
Dla pobranych liczb 2, 4 i 6, funkcja powinna zwrocic liczbe 4.

"""


def srednia_arytmetyczna(n):
    suma = 0
    for i in range(n):
        liczba = int(input("Podaj liczbe: "))
        suma += liczba
    return suma / n


if __name__ == "__main__":

    n = int(input("Podaj liczbe: "))
    print(srednia_arytmetyczna(n))
