"""
Otrzymujesz dokładnie 6 liczb. Otrzymane liczby stanowią odpowiednio 
współrzędne xA, yA, xB, yB, xC, yC. Sprawdź czy punkty A, B oraz C 
mogą stanowić wierzchołki trójkąta. 
"""

def czy_trojkat(lista):
    xA, yA, xB, yB, xC, yC = lista

    a = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
    b = ((xC - xB) ** 2 + (yC - yB) ** 2) ** 0.5
    c = ((xA - xC) ** 2 + (yA - yC) ** 2) ** 0.5

    if a + b > c and a + c > b and b + c > a:
        return True

    return False

def test_czy_trojkat():
    assert not czy_trojkat([1, 1, 1, 1, 1, 1])
    assert not czy_trojkat([0, 0, 2, -2, 5, -5])
    assert czy_trojkat([-2, 4,  7, 5, 8, -8])

if __name__ == "__main__":
    
    test_czy_trojkat()
