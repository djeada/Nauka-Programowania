"""
Napisz klase Ptak, dziedziczaca po klasach Zwierz oraz ObiektLatajacy. 
a) W sklad klasy Zwierz powinny wchodzic funkcje wypisujace na standardowe 
wyjscie komunikaty odpowiadajace ich nazwom. Funkcje powinny miec 
nastepujace nazwy: jedz(), spij(), wydaj_dzwiek(). 
b) W sklad klasy ObiektLatajacy powinny wchodzic funkcje wypisujace na 
standardowe wyjscie komunikaty odpowiadajace ich nazwom. Funkcje powinny 
miec nastepujace nazwy: lec(), wyladuj().
"""


class Zwierz:

    def __init__(self, name):
        self.name = name

    def jedz(self):
        print(f"{self.name} jedzie")

    def spij(self):
        print(f"{self.name} spi")

    def wydaj_dzwiek(self):
        print(f"{self.name} wydaje dzwiek")


class ObiektLatajacy:

    def __init__(self, name):
        self.name = name

    def lec(self):
        print(f"{self.name} leci")

    def wyladuj(self):
        print(f"{self.name} wylada")


class Ptak(Zwierz, ObiektLatajacy):
    
        def __init__(self, name):
            Zwierz.__init__(self, name)
            ObiektLatajacy.__init__(self, name)
        

if __name__ == "__main__":

    ptak = Ptak("Dziobak")
    ptak.jedz()
    ptak.spij()
    ptak.wydaj_dzwiek()
    ptak.lec()
    ptak.wyladuj()