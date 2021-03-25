"""
Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.
"""

if __name__ == "__main__":

    print("podaj dwie liczby")

    a = int(input())
    b = int(input())

    if a < b:
        print(b)
        print(a)
        print(" druga liczba jest wieksza od pierwszej")
    else:
        print(a)
        print(b)
        print("druga liczba nie jest wieksza od pierwszej")
