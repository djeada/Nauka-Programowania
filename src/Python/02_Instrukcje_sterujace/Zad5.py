"""
Dla pobranych trzech liczb, wypisz je w kolejnosci rosnacej.
"""

if __name__ == "__main__":

    print("podaj trzy liczby")

    a = int(input())
    b = int(input())
    c = int(input())

    if a >= b and a >= c:
        if b >= c:
            print(c, b, a)
        else:
            print(b, c, a)

    elif c >= b and c >= a:
        if a >= b:
            print(b, a, c)
        else:
            print(a, b, c)

    else:
        if a >= c:
            print(c, a, b)
        else:
            print(a, c, b)
