"""
Napisz funkcję, która dla otrzymanej liczby wypisze zaczynając 
od podstawy trójkąt prostokątny równoboczny o wysokości równej 
otrzymanej liczbie.
"""


def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc - i):
            print("*", end=" ")
        print()


if __name__ == "__main__":

    print("Podaj wysokość trojkata: ")
    wysokosc = int(input())

    trojkat(wysokosc)
