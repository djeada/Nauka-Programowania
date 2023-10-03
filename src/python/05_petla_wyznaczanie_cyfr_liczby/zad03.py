"""
Tytul: Tresc: Dla otrzymanej liczby naturalnej wypisz sume cyfr tej liczby.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanej liczby 129, powinna zostac wypisana liczba 12.

"""

if __name__ == "__main__":

    liczba = int(input("Podaj liczbe: "))

    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10

    print(f"Suma cyfr wynosi: {suma}")
