"""
Tytul: Cyfry liczby spelniajace okreslone warunki.
Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry tej liczby, ktore sa:
a) liczbami parzystymi,
b) mniejsze niz 5,
c) rozne od 0.
Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
Dane wyjsciowe: Kilka liczb.
Przyklad:
a) Dla otrzymanej liczby 932, powinna zostac wypisana liczba 2.
b) Dla otrzymanej liczby 101, powinny zostac wypisane liczby 1, 0 i 1.
c) Dla otrzymanej liczby 650, powinny zostac wypisane liczby 6 i 5.

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
