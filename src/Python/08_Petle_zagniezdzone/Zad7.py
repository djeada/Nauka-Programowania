"""
Napisz funkcje, ktora dla otrzymanej liczby N, wypisze N trojkatow. 
Trojkaty powinny byc ustawione w kolumnie, jeden na drugim. Wysokosc 
pierwszego trojkata to 1, a kazdego nastepnego rowna jest wysokosci 
poprzedniego powiekszonej o 1.
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
