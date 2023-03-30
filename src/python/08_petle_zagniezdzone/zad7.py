"""
Tytul: Choinka.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N trojkatow ustawionych w kolumnie, jeden na drugim. Wysokosc pierwszego trojkata to 1, a kazdego nastepnego jest rowna wysokosci poprzedniego powiekszonej o 1.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 3 powinno zostac wypisane:
*
*
**
*
**
***

"""

def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(i + 1):
            print("*", end="")
        print()

def choinka(wysoksoc):
    for i in range(1, wysoksoc + 1):
        trojkat(i)

if __name__ == "__main__":

    print("Podaj wysokosc choinki: ")
    wysokosc = int(input())

    choinka(wysokosc)

