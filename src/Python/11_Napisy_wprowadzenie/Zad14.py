"""
Stworz napis skladajacy sie z liczb od 1 do n.	
"""

# Wersja 1
def liczby_do_nv1(n):
    return "".join([str(i) for i in range(1, n + 1)])


# Wersja 2
def liczby_do_nv2(n):

    wynik = ""

    for i in range(n):
        wynik += str(1 + i)

    return wynik


# Testy Poprawnosci
assert liczby_do_nv1(3) == "123"
assert liczby_do_nv2(3) == "123"

assert liczby_do_nv1(-1) == ""
assert liczby_do_nv2(-1) == ""
