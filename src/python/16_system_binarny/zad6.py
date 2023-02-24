import math

"""
Otrzymujesz liczbe naturalna, podstawe systemu liczbowego w ktorym 
zapisana jest otrzymana liczba oraz podstawe systemu na ktory ma 
zostac dokonana konwersja. Zwroc reprezentacje otrzymanej liczby 
w nowym systemie.
"""


def na_dziesietny(liczba, stara_podstawa):
    """
    Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na reprezentacje w systemie dziesietnym.
    """
    reprezentacja_dziesietna = 0

    for i in range(len(liczba) - 1, -1, -1):

        if liczba[i] >= "A" and liczba[i] < "Z":
            reprezentacja_dziesietna += (ord(liczba[i]) - ord("A") + 10) * math.pow(
                stara_podstawa, (len(liczba) - 1 - i)
            )
        else:
            reprezentacja_dziesietna += (ord(liczba[i]) - ord("0")) * math.pow(
                stara_podstawa, (len(liczba) - 1 - i)
            )

    return int(reprezentacja_dziesietna)


def zmien_podstawe(liczba, stara_podstawa, nowa_podstawa):
    """
    Funkcja zamienia liczbe z reprezentacji w systemie stara_podstaw na 
    reprezentacje w systemie nowa_podstawa.
    """

    if stara_podstawa > (10 + ord("Z") - ord("A")):
        raise ValueError("Stara podstawa jest za duza")

    reprezentacja_dziesietna = na_dziesietny(liczba, stara_podstawa)
    liczba = ""
    podstawa = nowa_podstawa

    while reprezentacja_dziesietna > 0:
        reszta = reprezentacja_dziesietna % podstawa
        reprezentacja_dziesietna //= podstawa

        nowy_znak = chr(ord("0") + reszta)

        if nowy_znak > "9":
            nowy_znak = "A" + (nowy_znak - "9") - 1

        liczba += nowy_znak

    return liczba[::-1]


def test_zmien_podstawe():
    assert zmien_podstawe("101", 2, 10) == "5"
    assert zmien_podstawe("101", 2, 16) == "5"
    assert zmien_podstawe("101", 10, 2) == "1100101"
    assert zmien_podstawe("101", 10, 16) == "65"
    assert zmien_podstawe("4301", 10, 4) == "1003031"


if __name__ == "__main__":
    test_zmien_podstawe()
