"""
Tytul: Wywolywanie metody klasy bazowej w klasie potomnej
Tresc: Dla dwoch dowolnych klas, gdzie jedna jest klasa bazowa, a druga potomna, wywolaj metode klasy bazowej w metodzie klasy potomnej, ktora ja nadpisuje. Napisz program testujacy te klasy.

"""


class Rodzic:
    def __init__(self):
        print("Jestem rodzicem")


class DzieckoA(Rodzic):
    def __init__(self):
        print("Jestem dzieckiem A")


class DzieckoB(Rodzic):
    def __init__(self):
        print("Jestem dzieckiem B")
        super().__init__()


if __name__ == "__main__":

    print("Tworze obiekt klasy Rodzic:")
    rodzic = Rodzic()

    print("\nTworze obiekt klasy DzieckoA:")
    dziecko_a = DzieckoA()

    print("\nTworze obiekt klasy DzieckoB:")
    dziecko_b = DzieckoB()
