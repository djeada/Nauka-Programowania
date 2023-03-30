"""
Tytuł: Kalkulator kredytowy
Treść: Pobierz roczną stopę procentową, liczbę lat na spłacenie kredytu oraz wysokość udzielonego kredytu. Oblicz miesięczną ratę oraz całkowity koszt kredytu.
Dane wejściowe: Trzy liczby naturalne.
Dane wyjściowe: Dwie liczby naturalne.
Przykład:
Dla pobranych liczb: 3.5 (roczna stopa procentowa), 8 (liczba lat) oraz 12000 (wysokość kredytu), powinny zostać wypisane liczby 143.5 (miesięczna rata) oraz 13776 (całkowity koszt kredytu). Waluta jest umowna.

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
