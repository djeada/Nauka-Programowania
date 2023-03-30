"""
Tytul: Cyfry liczby.
Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry, z ktorych sie sklada, zaczynajac od cyfry jednosci.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczby.
Przyklad:
Dla otrzymanej liczby 8214, powinny zostac wypisane cyfry 4, 1, 2 i 8.

"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    while liczba > 0:
        print(liczba % 10)
        liczba = liczba // 10

