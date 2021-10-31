import string

"""
Policz z ilu słów składa się zdanie. Znaki interpunkcyjne nie są liczone jako słowa.
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def liczba_slow_w_zdaniu(zdanie):
    return len(podziel_zdanie_na_slowa(zdanie))


def test_liczba_slow_w_zdaniu():
    assert liczba_slow_w_zdaniu("Ala ma kota.") == 3
    assert liczba_slow_w_zdaniu("Ala ma kota, a kot ma Alę.") == 7


if __name__ == "__main__":
    test_liczba_slow_w_zdaniu()
