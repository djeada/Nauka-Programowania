"""
Otrzymujesz dwie listy liczb całkowitych. Zbuduj słownik składający się z 
kluczy będących elementami pierwszej listy i wartościami będącymi elementami 
drugiej listy. Jeśli listy są różnej długości zwróć pusty słownik.
"""

def stworz_slownik(lista_a, lista_b):
    """
    Funkcja tworzy słownik zawierający klucze będące elementami 
    pierwszej listy i wartości będące elementami drugiej listy.
    """

    if len(lista_a) != len(lista_b):
        return {}

    return dict(zip(lista_a, lista_b))

def test_stworz_slownik():
    assert stworz_slownik([1, 2, 3], [4, 5, 6]) == {1: 4, 2: 5, 3: 6}
    assert stworz_slownik([1, 2, 3], [4, 5]) == {}


if __name__ == "__main__":

    test_stworz_slownik()

