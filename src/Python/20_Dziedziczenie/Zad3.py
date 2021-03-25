"""
Polimorfizm.
"""


class Zwierz:
    def __init__(self, nazwa, dzwiek):
        self.nazwa = nazwa
        self.dzwiek = dzwiek

    def __repr__(self):
        return "nazwa : %s  dzwiek : %s" % (self.nazwa, self.dzwiek)

    def getDzwiek(self):
        return self.dzwiek

    def getTyp(self):
        print("Zwierz")


class Pies(Zwierz):
    def __init__(self, nazwa, dzwiek, dom):
        self.dom = dom
        super(Pies, self).__init__(nazwa, dzwiek)

    def __repr__(self):
        return "nazwa : %s  dzwiek : %s  dom : %s" % (self.nazwa, self.dzwiek, self.dom)

    def getTyp(self):
        print("Pies")

    def wydajOdglosy(self):
        print(self.dzwiek)
        print(self.dzwiek)


class JakiZwierz(object):
    def getTyp(self, objType):
        objType.getTyp()


a = Zwierz("tajemny zwierz", "xxx")
b = Pies("Burek", "Hau", "sklep")
c = JakiZwierz()

print(a)
print(b)
b.wydajOdglosy()
c.getTyp(a)
c.getTyp(b)
