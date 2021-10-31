"""
Napisz funkcję, która zwróci:

a) Liczbę 3.
b) Napis “Tak”.
c) Wartość logiczną Prawda.
"""


def zwroc_3():
    return 3


def zwroc_tak():
    return "Tak"


def zwroc_prawda():
    return True


def test_zwroc_3():
    assert zwroc_3() == 3


def test_zwroc_tak():
    assert zwroc_tak() == "Tak"


def test_zwroc_prawda():
    assert zwroc_prawda() == True


if __name__ == "__main__":

    test_zwroc_3()
    test_zwroc_tak()
    test_zwroc_prawda()
