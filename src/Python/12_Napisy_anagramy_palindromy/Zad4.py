import string

"""
Otrzymujesz napis reprezentujący zdanie. Znajdź wszystkie palindromy 
w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.
"""

def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja rozdziela zdanie na słowa. 
    """
    return zdanie.translate(str.maketrans('', '', string.punctuation)).split()

def czy_palindrom(slowo):
    """
    Funkcja sprawdza czy podane słowo jest palindromem. 
    """
    return slowo == slowo[::-1]

def palindromy_w_zdaniu(zdanie):
    """
    Funkcja zwraca listę palindromów w podanym zdaniu. 
    """
    return [slowo for slowo in podziel_zdanie_na_slowa(zdanie) if czy_palindrom(slowo)]

def test_palindromy_w_zdaniu():
    assert sorted(palindromy_w_zdaniu('Tata zbaral kajak na wycieczke i uderzyl sie w oko')) == sorted(["kajak", "i", "w", "oko"])

if __name__ == "__main__":
    test_palindromy_w_zdaniu()    