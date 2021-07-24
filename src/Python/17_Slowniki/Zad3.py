"""
Wypisz slownik posortowany wzgledem kluczy.	
"""

# Wersja 1
def sortuj_slownik_wzgledem_kluczy_v1(slownik):
    return {k: v for k, v in sorted(slownik.items(), key=lambda x: x[0])}


# Wersja 2
def sortuj_slownik_wzgledem_kluczy_v2(slownik):
    lista = sorted(slownik.items(), key=lambda x: x[0])
    return {x[0]: x[1] for x in lista}


# Testy poprawnosci
slownik = {"c": 5, "g": 9, "e": 4, "a": 2, "b": -1}
wynik = {"a": 2, "b": -1, "c": 5, "e": 4, "g": 9}

assert sortuj_slownik_wzgledem_kluczy_v1(slownik) == wynik
assert sortuj_slownik_wzgledem_kluczy_v2(slownik) == wynik

"""
Wypisz slownik posortowany wzgledem wartosci.	
"""


def sortuj_slownik_wzgledem_wartosci_v1(slownik):
    return {k: v for k, v in sorted(slownik.items(), key=lambda x: x[1])}


def sortuj_slownik_wzgledem_wartosci_v2(slownik):
    lista = sorted(slownik.items(), key=lambda x: x[1])
    return {x[0]: x[1] for x in lista}


# Testy poprawnosci
slownik = {3: 5, "hej": 9, "e": 4, "xxx": 2, 1: -1}
wynik = {1: -1, "xxx": 2, "e": 4, 3: 5, "hej": 9}

assert sortuj_slownik_wzgledem_wartosci_v1(slownik) == wynik
assert sortuj_slownik_wzgledem_wartosci_v2(slownik) == wynik
