"""
Tytul: Obliczanie wynikow operacji arytmetycznych.
Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze wyniki nastepujacych operacji arytmetycznych:
a) suma tych liczb
b) roznica pierwszej i drugiej liczby
c) iloczyn tych liczb
d) iloraz pierwszej liczby przez druga
e) reszta z dzielenia pierwszej liczby przez druga
f) pierwsza liczba podniesiona do potegi rownej drugiej liczbie
Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
* Jesli uzytkownik poda liczby 9 oraz 1, program powinien wypisac liczby: 10, 1, 9, 9, 0, 9.
* Jesli uzytkownik poda liczby 3 oraz 2, program powinien wypisac liczby: 5, 1, 6, 1, 1, 9.

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

