"""
Otrzymujesz napis. Znajdz znaki znajdujace sie na 
pozycjach bedacych liczbami pierwszymi.
"""


def czy_pierwsza(liczba):
    if liczba <= 1:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def znaki_na_pozycjach_pierwszych(napis):
    znaki = []
    for i, znak in enumerate(napis):
        if czy_pierwsza(i):
            znaki.append(znak)
    return znaki


def test_znaki_na_pozycjach_pierwszych():
    assert znaki_na_pozycjach_pierwszych("abcd") == ["c", "d"]
    assert znaki_na_pozycjach_pierwszych("Kaczka lubi wiosne.") == [
        "c",
        "z",
        "a",
        "l",
        " ",
        "i",
        "e",
    ]


if __name__ == "__main__":

    test_znaki_na_pozycjach_pierwszych()
