"""
Tytul: Prostokat powstaly z nalozenia sie dwoch prostokatow.
Opis zadania: Napisz klase Prostokat, ktora bedzie reprezentowala prostokat w ukladzie kartezjanskim. Prostokat jest okreslony przez wspolrzedne jego czterech wierzcholkow. Boki prostokata sa prostopadle do osi ukladu wspolrzednych. Klasa powinna zawierac funkcje statyczna, ktora zwraca pole prostokata powstalego z nalozenia sie dwoch prostokatow. Jesli dwa prostokaty nie pokrywaja sie, funkcja powinna zwracac 0.
Napisz program, ktory przetestuje twoja klase. Stworz prostokaty: A (3, 6, 9, 4) oraz B (2, 5, 7, 2). Wypisz na standardowe wyjscie informacje o utworzonych prostokatach. Sprawdz, czy pole czesci wspolnej rowne jest 6.

"""

class Prostokat:
    def __init__(self, lewo, gora, prawo, dol):
        self.lewo = lewo
        self.gora = gora
        self.prawo = prawo
        self.dol = dol

    def pole(self):
        return (self.prawo - self.lewo) * (self.dol - self.gora)

    @staticmethod
    def pole_czesci_wspolnej(p1, p2):
        if (
            p1.lewo > p2.prawo
            or p1.prawo < p2.lewo
            or p1.gora < p2.dol
            or p1.dol > p2.gora
        ):
            return 0

        pole_x = max(0, min(p1.prawo, p2.prawo) - max(p1.lewo, p2.lewo))
        pole_y = max(0, min(p1.gora, p2.gora) - max(p1.dol, p2.dol))

        return pole_x * pole_y

def test_pole_czesci_wspolnej_pozytwne():
    prostokat_a = Prostokat(2, 7, 5, 2)
    prostokat_b = Prostokat(3, 9, 6, 4)
    wynik = 6
    assert Prostokat.pole_czesci_wspolnej(prostokat_a, prostokat_b) == wynik

def test_pole_czesci_wspolnej_negatywne():
    prostokat_a = Prostokat(1, 1, -1, -1)
    prostokat_b = Prostokat(2, 2, 1, 1)
    wynik = 0
    assert Prostokat.pole_czesci_wspolnej(prostokat_b, prostokat_a) == wynik

if __name__ == "__main__":
    test_pole_czesci_wspolnej_pozytwne()
    test_pole_czesci_wspolnej_negatywne()

