"""
Dla dwoch slow, ile minimalnie znakow musimy usunac aby uzyskac anagramy.
Zwroc -1 dla slow, o roznych dlugosciach.	
"""

# Wersja 1
def budujHistogramZnakow(slowo):
    histo = {}

    for znak in slowo:
        if znak in histo:
            histo[znak] += 1
        else:
            histo[znak] = 0

    return histo


def minZnakowDoZmianyV1(slowoA, slowoB):
    if len(slowoA) != len(slowoB):
        return -1

    histoSlowaA = budujHistogramZnakow(slowoA)
    histoSlowaB = budujHistogramZnakow(slowoB)
    licznik = 0

    for klucz, wartosc in histoSlowaA.items():
        if klucz not in histoSlowaB.keys():
            licznik += 1
        else:
            licznik += wartosc - histoSlowaB[klucz]

    for klucz, wartosc in histoSlowaB.items():
        if klucz not in histoSlowaA.keys():
            licznik += 1
        else:
            licznik += wartosc - histoSlowaA[klucz]

    return licznik


# Testy Poprawnosci
slowoA = "grazyna"
slowoB = "razynax"
assert minZnakowDoZmianyV1(slowoA, slowoB) == 2

slowoA = "pancytryna"
slowoB = "panpomarancza"
assert minZnakowDoZmianyV1(slowoA, slowoB) == -1

slowoA = "20ejdy0978oa"
slowoB = "akv81w39j1o7"
assert minZnakowDoZmianyV1(slowoA, slowoB) == 10
