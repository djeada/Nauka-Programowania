"""
Tytul: Wypisz co k-ty znak napisu poziomo i pionowo.
Tresc: Otrzymasz napis oraz liczbe k.
a) Wypisz co k-ty znak napisu poziomo, rozdzielajac znaki spacjami.
b) Wypisz co k-ty znak napisu pionowo, rozdzielajac znaki enterami.
Dane wejsciowe: Napis oraz liczba.
Dane wyjsciowe: Napis.
Przyklad:
a) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis: "z h n".
b) Dla otrzymanego napisu: "Grzechotnik" oraz liczby 3, powinien zostac zwrocony napis:
z
h
n

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

