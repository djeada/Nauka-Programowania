"""
Wywolaj metode klasy bazowej w metodzie klasy potomnej nadipsujacej ta metode.
"""

# Wersja 1
class Rodzic:
    def __init__(self):
        print("Jestem rodzicem")


class DzieckoA(Rodzic):
    def __init__(self):
        print("Jestem dzieckiem A")


class DzieckoB(Rodzic):
    def __init__(self):
        print("Jestem dzieckiem B")
        super(DzieckoB, self).__init__()


rodzic = Rodzic()
dzieckoA = DzieckoA()
dzieckoB = DzieckoB()
