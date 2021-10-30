"""
Dla pobranej liczby, sprawdź czy jest ona palindromem. 
To znaczy, sprawdź czy liczba nie zmienia się po zapisaniu 
jej cyfr w odwrotnej kolejności.
"""

if __name__ == "__main__":

    print("Podaj liczbę: ")
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

