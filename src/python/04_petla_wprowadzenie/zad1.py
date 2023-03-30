"""
Tytul: Warunek konczacy petle.
Tresc: Pros uzytkownika o podanie liczby, dopoki nie zostanie podana liczba 7.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.

"""

if __name__ == "__main__":

    liczba = 0

    while liczba != 7:
        liczba = int(input("Podaj liczbe: "))

