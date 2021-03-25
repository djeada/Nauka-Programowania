"""
Posortuj liste obiektow wzgledem jednego z atrybutow.
"""


class Miasto:
    def __init__(self, nazwa, liczbaMieszkancow):
        self.nazwa = nazwa
        self.liczbaMieszkancow = liczbaMieszkancow

    def __repr__(self):
        return self.nazwa + " : " + str(self.liczbaMieszkancow)


miasta = [
    Miasto("New York", 8400000),
    Miasto("Paris", 2150000),
    Miasto("Berlin", 3800000),
]

import operator

for miasto in sorted(miasta, key=operator.attrgetter("nazwa")):
    print(miasto)

for miasto in sorted(miasta, key=operator.attrgetter("liczbaMieszkancow")):
    print(miasto)
