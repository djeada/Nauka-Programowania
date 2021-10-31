import string

"""
Otrzymujesz napis reprezentujący zdanie. Podziel zdanie na słowa składowe. 
Wypisz pionowo słowa, z których składa się zdanie. Znaki interpunkcyjne 
nie są liczone jako słowa.
"""

def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans('', '', string.punctuation)).split()

def wypisz_pionowo(zdanie):
    for slowo in podziel_zdanie_na_slowa(zdanie):
        print(slowo)

if __name__ == "__main__":
    zdanie = "Ala ma kota, a kot ma Ale."
    wypisz_pionowo(zdanie)
