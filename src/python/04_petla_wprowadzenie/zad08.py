"""
Tytul: Liczba kur i owiec na farmie.
Tresc: Na farmie jest a glow i b nog. Znajdz liczbe kur i liczbe owiec.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Dwie liczby naturalne.
Przyklad:
Dla otrzymanych liczb 40 i 100, powinny zostac wypisane liczby 30 i 10.

"""

if __name__ == "__main__":

    glowy = int(input("Podaj liczbe glow: "))
    nogi = int(input("Podaj liczbe nog: "))

    kury = 0
    owieczki = 0

    for i in range(glowy):
        owieczki = glowy - i
        if 2 * i + 4 * owieczki == nogi:
            print("Liczba kur: ", i)
            print("Liczba owieczek: ", owieczki)
            break
