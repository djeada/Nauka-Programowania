"""
N krążków o różnych średnicach ułożone jest na jednym z trzech słupków 
(A, B lub C). Na spodzie znajduje się krążek o największej średnicy. 
Każdy następny krążek jest mniejszy od poprzedniego. Znajdź sposób na 
przełożenie wszystkich krążków na inny słupek. Pamiętaj, że nie wolno 
kłaść krążka o większej średnicy na krążek o mniejszej średnicy, ani 
przekładać kilku krążków jednocześnie. 
"""

def hanoi(n):
    """
    Funkcja zwraca listę ruchów, które powinny być wykonane, aby 
    przełożyć n krążków ze słupka A na słupek B. Słupek C jest
    słupkiem pomocniczym.
    """
    def hanoi_rek(n, from_tower, to_tower, aux_tower, wynik):
        """
        Rekurencyjna funkcja wewnętrzna.
        """
        if n == 1:
            wynik.append((from_tower, to_tower))
        else:
            hanoi_rek(n-1, from_tower, aux_tower, to_tower, wynik)
            hanoi_rek(1, from_tower, to_tower, aux_tower, wynik)
            hanoi_rek(n-1, aux_tower, to_tower, from_tower, wynik)
        return wynik
    
    wynik = list()
    hanoi_rek(n, 'A', 'B', 'C', wynik)
    return wynik

def test_hanoi():
    assert hanoi(1) == [('A', 'B')]
    assert hanoi(2) == [('A', 'C'), ('A', 'B'), ('C', 'B')]
    assert hanoi(3) == [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]

if __name__ == "__main__":
    test_hanoi()
