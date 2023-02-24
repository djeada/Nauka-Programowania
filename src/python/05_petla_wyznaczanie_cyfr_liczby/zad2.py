"""
Dla pobranej liczby, powinny zostac wypisane 
cyfry pobranej liczby zaczynajac od cyfry jednosci.
"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    while liczba > 0:
        print(liczba % 10)
        liczba = liczba // 10
