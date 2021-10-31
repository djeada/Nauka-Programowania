"""
Napisz funkcję, która dla otrzymanej liczby N, 
wypisze N pierwszych wierszy i kolumn tabliczki 
mnożenia.
"""

def tabliczka_mnozenia(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end=' ')
        print()

if __name__ == "__main__":

    print("Podaj liczbę: ")
    n = int(input())

    tabliczka_mnozenia(n)
    