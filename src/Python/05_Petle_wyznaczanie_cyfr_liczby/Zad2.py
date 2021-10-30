"""
Dla pobranej liczby, powinny zostać wypisane 
cyfry pobranej liczby zaczynając od cyfry jedności.
"""

if __name__ == "__main__":

    print("Podaj liczbę: ")
    liczba = int(input())

    while liczba > 0:
        print(liczba % 10)
        liczba = liczba // 10
