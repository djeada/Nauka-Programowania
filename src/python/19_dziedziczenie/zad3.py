"""
Tytul: Polimorfizm.
Tresc: Zaprojektuj klase Zwierz oraz klasy potomne Pies i Kot. Obie klasy potomne powinny nadpisywac metode 'odglos()' zdefiniowana w klasie bazowej. Napisz program testujacy te klasy, w ktorym umiescisz obiekty wszystkich trzech klas w jednej liscie i przejdziesz przez wszystkie elementy tej listy, wywolujac dla kazdego z nich funkcje 'odglos()'."

"""


class Zwierz:
    def __init__(self, imie):
        self.imie = imie

    def odglos(self):
        print("Odglos zwierzecia")

    def __str__(self):
        return self.imie


class Pies(Zwierz):
    def odglos(self):
        print("Hau hau")


class Kot(Zwierz):
    def odglos(self):
        print("Miau miau")


if __name__ == "__main__":
    zwierzeta = [Zwierz("Zwierz"), Pies("Piesek"), Kot("Kotek")]
    for zwierze in zwierzeta:
        print(f"{zwierze} wydaje odglos:")
        zwierze.odglos()

