"""
Otrzymujesz listę liczb naturalnych oraz klucz.
Przy użyciu rekurencji znajdź indeks odpowiadający 
pierwszemu wystąpieniu klucza w liście. Jeśli 
klucz nie wystęþuje w liście, zwróć -1.
"""

def wyszukiwani_liniowe(lista, klucz):
    """
    Funkcja zwraca indeks klucza w liście przy pomocy rekurenkcji.
    Jeśli klucz nie występuje w liście, zwróć -1.
    """
    if len(lista) == 0:
        return -1
    
    if lista[0] == klucz:
        return 0
    
    if wyszukiwani_liniowe(lista[1:], klucz) != -1:
        return 1 + wyszukiwani_liniowe(lista[1:], klucz)

    return -1


def test_wyszukiwani_liniowe():
    assert wyszukiwani_liniowe([1, 2, 3, 4, 5], 3) == 2
    assert wyszukiwani_liniowe([1, 2, 3, 4, 5], 6) == -1

if __name__ == "__main__":
    
    test_wyszukiwani_liniowe()