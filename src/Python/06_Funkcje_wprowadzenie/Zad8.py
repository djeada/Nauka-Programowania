import random

"""
Napisz funkcję realizującą zaokrąglanie ilorazu bez użycia '/' i '%'.
"""

# Wersja 1
def podziel(a, b):

    znak = 1

    if b == 0:
        return float("nan")

    if a == 0:
        return 0

    if a < 0:
        znak = -1
        a = -a

    if b < 0:
        znak *= -1
        b = -b

    if znak == 1:
        licznik = 0
        while a >= b:
            a -= b
            licznik += 1

    else:
        licznik = 1
        while a > b:
            a -= b
            licznik += 1

    return licznik * znak


# Testy Poprawnosci
def losowa(a, b):
    return int(b + random.random() * (a - b))


for i in range(10):
    a = losowa(-20, 20)
    b = losowa(-20, 20)

    while b == 0:
        b = losowa(-20, 20)

    assert podziel(a, b) == a // b
