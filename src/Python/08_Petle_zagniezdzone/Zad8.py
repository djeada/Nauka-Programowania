from math import pow

"""
Napisz funkcję, która dla otrzymanej liczby wypisze 
trójkąt Pascala o wysokości równej otrzymanej liczbie.
"""


def trojkat_pascala(wysokosc):

    for i in range(wysokosc):
        for j in range(i + 1):
            print(pow(2, i) - pow(2, i - j) + pow(2, j), end=" ")
    print()


if __name__ == "__main__":

    print("Podaj wysokość trojkata Pascala: ")
    wysokosc = int(input())
    trojkat_pascala(wysokosc)
