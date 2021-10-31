import string

"""
Otrzymujesz napis reprezentujący zdanie. Znajdź: 
a) Najdłuższe słowo w zdaniu.
b) Najkrótsze słowo w zdaniu. 

Jeśli więcej niż jedno słowo ma ekstremalną długość, zwróć to 
słowo spośród nich, które występuje w zdaniu jako pierwsze. 
Znaki interpunkcyjne nie są liczone jako słowa.  
"""

def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans('', '', string.punctuation)).split()

def najdluzsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return max(slowa, key=len)

def najkrotsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return min(slowa, key=len)

def test_najdluzsze_slowo():
    assert najdluzsze_slowo("Ala ma kota.") == "kota"

def test_najkrotsze_slowo():
    assert najkrotsze_slowo('Ala ma kota.') == "ma"

if __name__ == "__main__":
    
    test_najdluzsze_slowo()
    test_najkrotsze_slowo()