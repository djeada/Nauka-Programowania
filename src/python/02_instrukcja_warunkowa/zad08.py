"""
Tytul: Warunek trojkata.
Tresc: Dla trzech pobranych od uzytkownika dlugosci bokow sprawdz, czy mozna z nich zbudowac trojkat. Jednostki sa umowne.
Dane wejsciowe: Trzy liczby naturalne oznaczajace dlugosci bokow trojkata.
Dane wyjsciowe: Komunikat o mozliwosci lub niemozliwosci zbudowania trojkata.
Przyklad:
Dla pobranych liczb: 1, 2 oraz 3, powinna zostac wypisana informacja, ze nie mozna zbudowac trojkata z podanych bokow.

"""

if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())

    if a + b > c and b + c > a and a + c > b:
        print("z podanych bokow mozna zbudowac trojkat")

    else:
        print("z podanych bokow nie mozna zbudowac trojkata")

