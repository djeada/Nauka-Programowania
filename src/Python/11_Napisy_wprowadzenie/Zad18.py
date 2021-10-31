import string

"""
Otrzymujesz napis reprezentujący zdanie. Zamień słowa zdania, na te 
same napisy zapisane wspak. Znaki interpunkcyjne nie są liczone jako słowa. 
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def odwroc(napis):
    return napis[::-1]


def odwroc_slowa(zdanie):

    wynik = " ".join([odwroc(slowo) for slowo in podziel_zdanie_na_slowa(zdanie)])

    for i, znak in enumerate(zdanie):
        if znak in string.punctuation:
            wynik = wynik[:i] + znak + wynik[i:]

    return wynik


def test_odwroc_slowa():
    assert odwroc_slowa("Ala ma kota.") == "alA am atok."


if __name__ == "__main__":

    test_odwroc_slowa()
