"""
Otrzymujesz liczbę naturalną. Zbuduj słownik składający się 
z kluczy będących kolejnymi liczbami naturalnymi mniejszymi 
od otrzymanej liczby oraz wartości będących kwadratami 
odpowiadających im kluczy.
"""

def stworz_slownik(n):
    """
    Funkcja tworzy słownik zawierający klucze będące kolejnymi 
    liczbami naturalnymi mniejszymi od podanej liczby n 
    oraz wartości będącymi kwadratami kluczy.
    """

    slownik = {}
    for i in range(n):
        slownik[i] = i ** 2
    return slownik

def test_stworz_slownik():
    assert stworz_slownik(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    assert stworz_slownik(0) == {}

if __name__ == "__main__":
    
    test_stworz_slownik()
