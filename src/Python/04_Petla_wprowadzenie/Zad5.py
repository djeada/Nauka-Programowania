"""
Dla pobranych dwóch liczb, powinny zostać wypisane:

a) Wszystkie liczby naturalne większe od mniejszej pobranej liczby 
i jednocześnie mniejsze od większej pobranej liczby. 
b) Wszystkie liczby naturalne podzielne przez 3 większe od mniejszej 
pobranej liczby i jednocześnie mniejsze od większej pobranej liczby.
"""

if __name__ == "__main__":

    print("Podaj dwie liczby: ")
    pierwsza_liczba = int(input())
    druga_liczba = int(input())

    print(
        "Liczby naturalne większe od mniejszej pobranej liczby i jednocześnie mniejsze od większej pobranej liczby:"
    )
    if pierwsza_liczba > druga_liczba:
        for i in range(druga_liczba, pierwsza_liczba + 1):
            print(i)
    else:
        for i in range(pierwsza_liczba, druga_liczba + 1):
            print(i)

    print("\n")
    print(
        "Liczby naturalne podzielne przez 3 większe od mniejszej pobranej liczby i jednocześnie mniejsze od większej pobranej liczby:"
    )

    if pierwsza_liczba > druga_liczba:
        for i in range(druga_liczba, pierwsza_liczba + 1):
            if i % 3 == 0:
                print(i)
    else:
        for i in range(pierwsza_liczba, druga_liczba + 1):
            if i % 3 == 0:
                print(i)
