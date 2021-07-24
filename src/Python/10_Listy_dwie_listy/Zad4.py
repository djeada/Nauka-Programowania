"""
Masz dane dwie listy: wagi oraz wartosci. Znajdz srednia wazona wartosci.
"""

# Wersja 1
def srednia_wazona_v1(wartosci, wagi):
    if len(wartosci) != len(wagi):
        return False

    suma = sum(wartosci)

    suma_iloczynow = 0

    for i in range(len(wartosci)):
        suma_iloczynow += wartosci[i] * wagi[i]

    return suma_iloczynow / suma


# Wersja 2
def srednia_wazona_v2(wartosci, wagi):
    if len(wartosci) != len(wagi):
        return False

    return sum([x * y for x, y in zip(wagi, wartosci)]) / sum(wartosci)


# Testy Poprawnosci
wartosci = [0, -23, -5, 2, -3, 4, 9]
wagi = [1, 2, 3, 4, 5, 6, 7]

assert srednia_wazona_v1(wartosci, wagi) == -1.1875
assert srednia_wazona_v2(wartosci, wagi) == -1.1875

wartosci = [2, 5, 0, 2, 1]
wagi = [0.2, 0.4, 0.1, 0.2, 0.1]

assert srednia_wazona_v1(wartosci, wagi) == 0.29
assert srednia_wazona_v2(wartosci, wagi) == 0.29
