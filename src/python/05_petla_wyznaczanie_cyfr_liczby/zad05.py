"""
Czy liczba jest palindromem?
Tresc: Dla otrzymanej liczby naturalnej sprawdz, czy jest ona palindromem, tj. czy nie zmienia sie po zapisaniu cyfr w odwrotnej kolejnosci.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 13231, powinna zostac wypisana informacja o tym, ze liczba jest palindromem.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    liczba_pomocnicza = liczba
    odwrocona = 0

    while liczba_pomocnicza > 0:
        odwrocona = odwrocona * 10 + liczba_pomocnicza % 10
        liczba_pomocnicza //= 10

    if liczba == odwrocona:
        print("Liczba jest palindromem.")
    else:
        print("Liczba nie jest palindromem.")

