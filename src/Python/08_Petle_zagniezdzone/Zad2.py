"""
Napisz funkcje, ktora dla otrzymanej liczby wypisze 
trojkat prostokatny rownoboczny o wysokosci rownej 
otrzymanej liczbie.
"""


def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(i + 1):
            print("*", end="")
        print()


if __name__ == "__main__":

    wysokosc = int(input("Podaj wysokosc trojkata: "))
    trojkat(wysokosc)
