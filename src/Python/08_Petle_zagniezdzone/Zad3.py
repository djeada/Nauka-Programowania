"""
Napisz funkcje, ktora dla otrzymanej liczby wypisze zaczynajac 
od podstawy trojkat prostokatny rownoboczny o wysokosci rownej 
otrzymanej liczbie.
"""


def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc - i):
            print("*", end=" ")
        print()


if __name__ == "__main__":

    print("Podaj wysokosc trojkata: ")
    wysokosc = int(input())

    trojkat(wysokosc)
