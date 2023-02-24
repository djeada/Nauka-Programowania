"""
Napisz funkcje, ktora dla otrzymanej liczby wypisze litere X, 
o wysokosci rownej otrzymanej liczbie.
"""


def litera_x(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc):
            if j == i or j == wysokosc - i - 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":

    print("Podaj wysokosc litery X: ")
    wysokosc = int(input())

    litera_x(wysokosc)
