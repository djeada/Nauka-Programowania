"""
Napisz funkcję, która dla otrzymanej liczby wypisze 
literę Z, o wysokości równej otrzymanej liczbie.
"""


def litera_z(wysokosc):
    for i in range(wysokosc):
        for j in range(wysokosc):
            if i == 0 or i == wysokosc - 1 or j == wysokosc - i - 1:
                print("Z", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":

    print("Podaj wysokość litery Z: ")
    wysokosc = int(input())

    litera_z(wysokosc)
