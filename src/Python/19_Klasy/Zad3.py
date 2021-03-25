"""
Otrzymujesz liste wspolrzednych wierzcholkow dwoch prostokatow.
Znajdz wspolrzedne prostokata powstalego z nalozenia sie dwoch innych prostokatpw.
"""


def Prostokat():
    def __init__(self, listaWspolrzednychWierzcholkow):
        self.listaWspolrzednychWierzcholkow = listaWspolrzednychWierzcholkow

    def wypisz(self):
        print("Wierzcholki prostokata: ")
        for punkt in listaWspolrzednychWierzcholkow:
            print(punkt)
