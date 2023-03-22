"""
Zaprojektuj klase Zwierz oraz klasy pochodne Pies oraz Kot. 
Obie klasy potomne powinny nadpisywac metode odglos() klasy 
zdefiniowana w klasie bazowej. Nastepnie w programie 
testujacym napisane klasy, nalezy w jednej liscie zebrac 
obiekty wszystkich trzech klas. Nalezy przy pomocy petli 
przejsc przez wszystkie elementy listy i dla kazdego z nich 
wywolac funkcje odglos().
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
        print(f'{zwierze} wydaje odglos:')
        zwierze.odglos()