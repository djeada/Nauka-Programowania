"""
Tytul: Liczby z okreslonego przedzialu.
Tresc: Dla otrzymanych dwoch liczb naturalnych wypisz:
a) Wszystkie liczby naturalne wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.
b) Wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Kilka liczb naturalnych.
Przyklad:
Dla otrzymanych liczb 9 i 5 powinny zostac wypisane liczby 6, 7 i 8.

"""

if __name__ == "__main__":

    print("Podaj dwie liczby: ")
    pierwsza_liczba = int(input())
    druga_liczba = int(input())

    print(
        "Liczby naturalne wieksze od mniejszej pobranej liczby i jednoczesnie mniejsze od wiekszej pobranej liczby:"
    )
    if pierwsza_liczba > druga_liczba:
        for i in range(druga_liczba, pierwsza_liczba + 1):
            print(i)
    else:
        for i in range(pierwsza_liczba, druga_liczba + 1):
            print(i)

    print("\n")
    print(
        "Liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej liczby i jednoczesnie mniejsze od wiekszej pobranej liczby:"
    )

    if pierwsza_liczba > druga_liczba:
        for i in range(druga_liczba, pierwsza_liczba + 1):
            if i % 3 == 0:
                print(i)
    else:
        for i in range(pierwsza_liczba, druga_liczba + 1):
            if i % 3 == 0:
                print(i)

