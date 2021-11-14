"""
Stworz klase Klasa. Klasa powinna zawierac funkcje statyczna zwracajaca 
aktualna liczbe instancji klasy w programie. Stworz kilka obiektow klasy 
i przetestuj dzialanie funkcji.
"""

class Klasa:
    liczba_instancji = 0

    def __init__(self):
        Klasa.liczba_instancji += 1

    def __del__(self):
        Klasa.liczba_instancji -= 1

if __name__ == "__main__":
    a = Klasa()
    b = Klasa()
    print(Klasa.liczba_instancji)
    del a
    del b
    print(Klasa.liczba_instancji)
