# Znajdz min/maks dwoch liczb bez uzycia instrukcji warunkowej.


def znak(n):
    return (n >> 31) & 0x01


# a >= b : znakA = 1, znakB = 0;
# a < b : znakA = 0, znakB = 1;
def maks2(a, b):
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_a * a + znak_b * b


def min2(a, b):
    znak_b = znak(a - b)
    znak_a = znak_b ^ 1
    return znak_b * a + znak_a * b


if __name__ == "__main__":

    a = 10
    b = 8

    wynik = a
    assert maks2(a, b) == wynik

    wynik = b
    assert min2(a, b) == wynik
