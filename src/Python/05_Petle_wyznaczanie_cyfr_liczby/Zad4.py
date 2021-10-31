"""
Dla pobranej liczby, powinne zostac wypisane cyfry liczb, ktore sa:

a) Liczbami parzystymi.
b) Mniejsze niz 5.
c) Rozne od 0.
"""

if __name__ == "__main__":

    print("Podaj liczbe: ")
    liczba = int(input())

    print("Parzyst cyfry: ")
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        if cyfra % 2 == 0:
            print(cyfra)

        kopia //= 10

    print("Cyfry mniejsze niz 5: ")
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        if cyfra < 5:
            print(cyfra)

        kopia //= 10

    print("Cyfry rozne od 0: ")
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        if cyfra != 0:
            print(cyfra)

        kopia //= 10
