"""
Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.
"""

if __name__ == "__main__":
    print("podaj liczbe")

    a = int(input())

    if a < 0:
        print("libczba jest ujemna")
    elif a > 0:
        print("liczba jest dodatnia")
    else:
        print("liczba jest zerem")
