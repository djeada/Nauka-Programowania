"""
Wypisz wynik następujących operacji arytmetycznych dla dwóch liczb pobranych od użytkownika:

a) Suma liczb.
b) Różnica pierwszej i drugiej liczby.
c) Iloczyn liczb.
d) Iloraz pierwszej liczby przez drugą.
e) Reszta z dzielenia pierwszej liczby przez drugą.
f) Pierwsza liczba podniesiona do potęgi równej drugiej liczbie.
"""

if __name__ == "__main__":

    x = int(input())
    y = int(input())

    print("Suma liczb: ", x + y)
    print("Różnica pierwszej i drugiej liczby: ", x - y)
    print("Iloczyn liczb: ", x * y)
    print("Iloraz pierwszej liczby przez drugą: ", x / y)
    print("Reszta z dzielenia pierwszej liczby przez drugą: ", x % y)
    print("Pierwsza liczba podniesiona do potęgi równej drugiej liczbie: ", x ** y)
