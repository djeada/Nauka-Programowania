import string

"""
Otrzymujesz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe. 
Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne 
nie sa liczone jako slowa.
"""


def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def wypisz_pionowo(zdanie):
    for slowo in podziel_zdanie_na_slowa(zdanie):
        print(slowo)


if __name__ == "__main__":
    zdanie = "Ala ma kota, a kot ma Ale."
    wypisz_pionowo(zdanie)
