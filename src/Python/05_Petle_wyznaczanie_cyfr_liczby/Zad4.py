"""
Dla pobranej liczby, powinne zostać wypisane cyfry liczb, które są:

a) Liczbami parzystymi.
b) Mniejsze niż 5.
c) Różne od 0.
"""

if __name__ == "__main__":

    print("Podaj liczbę: ")
    liczba = int(input())

    print("Parzyst cyfry: ")
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        if cyfra % 2 == 0:
            print(cyfra)

        kopia //= 10

    print("Cyfry mniejsze niż 5: ")
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        if cyfra < 5:
            print(cyfra)

        kopia //= 10
    
    print("Cyfry różne od 0: ")
    kopia = liczba
    while kopia > 0:
        cyfra = kopia % 10
        if cyfra != 0:
            print(cyfra)

        kopia //= 10