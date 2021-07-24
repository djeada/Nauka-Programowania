"""
Polimorfizm.
"""


class Zwierz:
    def __init__(self, nazwa, dzwiek):
        self.nazwa = nazwa
        self.dzwiek = dzwiek

    def __repr__(self):
        return "nazwa : %s  dzwiek : %s" % (self.nazwa, self.dzwiek)

    def get_dzwiek(self):
        return self.dzwiek

    def get_typ(self):
        print("Zwierz")


class Pies(Zwierz):
    def __init__(self, nazwa, dzwiek, dom):
        self.dom = dom
        super(Pies, self).__init__(nazwa, dzwiek)

    def __repr__(self):
        return "nazwa : %s  dzwiek : %s  dom : %s" % (self.nazwa, self.dzwiek, self.dom)

    def get_typ(self):
        print("Pies")

    def wydaj_odglosy(self):
        print(self.dzwiek)
        print(self.dzwiek)


class JakiZwierz(object):
    def get_typ(self, obj_type):
        obj_type.get_typ()


a = Zwierz("tajemny zwierz", "xxx")
b = Pies("Burek", "Hau", "sklep")
c = JakiZwierz()

print(a)
print(b)
b.wydaj_odglosy()
c.get_typ(a)
c.get_typ(b)
