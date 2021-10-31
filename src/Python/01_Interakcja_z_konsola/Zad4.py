"""
Wypisz wynik nastepujacych operacji arytmetycznych dla dwoch liczb pobranych od uzytkownika:

a) Suma liczb.
b) Roznica pierwszej i drugiej liczby.
c) Iloczyn liczb.
d) Iloraz pierwszej liczby przez druga.
e) Reszta z dzielenia pierwszej liczby przez druga.
f) Pierwsza liczba podniesiona do potegi rownej drugiej liczbie.
"""

if __name__ == "__main__":

    x = int(input())
    y = int(input())

    print("Suma liczb: ", x + y)
    print("Roznica pierwszej i drugiej liczby: ", x - y)
    print("Iloczyn liczb: ", x * y)
    print("Iloraz pierwszej liczby przez druga: ", x / y)
    print("Reszta z dzielenia pierwszej liczby przez druga: ", x % y)
    print("Pierwsza liczba podniesiona do potegi rownej drugiej liczbie: ", x ** y)
