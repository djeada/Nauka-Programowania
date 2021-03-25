"""
Stworz napis skladajacy sie z liczb od 1 do n.	
"""

# Wersja 1
def liczbyDoNV1(n):
    return "".join([str(i) for i in range(1, n + 1)])


# Wersja 2
def liczbyDoNV2(n):

    wynik = ""

    for i in range(n):
        wynik += str(1 + i)

    return wynik


# Testy Poprawnosci
assert liczbyDoNV1(3) == "123"
assert liczbyDoNV2(3) == "123"

assert liczbyDoNV1(-1) == ""
assert liczbyDoNV2(-1) == ""
