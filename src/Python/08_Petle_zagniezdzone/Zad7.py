"""
Napisz funkcję, która dla otrzymanej liczby N, wypisze N trójkątów. 
Trójkąty powinny być ustawione w kolumnie, jeden na drugim. Wysokość 
pierwszego trójkąta to 1, a każdego następnego równa jest wysokości 
poprzedniego powiększonej o 1.
"""

def trojkat(wysokosc):
    for i in range(wysokosc):
        for j in range(i+1):
            print("*", end="")
        print()

def choinka(wysoksoc):
    for i in range(1, wysoksoc + 1):
        trojkat(i)

if __name__ == "__main__":
    
    print("Podaj wysokość choinki: ")
    wysokosc = int(input())

    choinka(wysokosc)