"""
Napisz funkcję, która dla otrzymanej liczby wypisze 
trójkąt prostokątny równoboczny o wysokości równej 
otrzymanej liczbie.
"""

def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(i+1):
            print("*", end="")
        print()

if __name__ == "__main__":

    wysokosc = int(input("Podaj wysokość trójkąta: "))
    trojkat(wysokosc)
    