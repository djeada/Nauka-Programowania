"""
Napisz funkcje, ktora dla otrzymanej liczby wypisze kwadrat 
o boku rownym otrzymanej liczbie.
"""


def kwadrat(bok):
    for i in range(bok):
        for j in range(bok):
            print("*", end="")
        print()


if __name__ == "__main__":

    bok = int(input("Podaj bok kwadratu: "))
    kwadrat(bok)
