"""
Zmodyfikuj napis w taki sposob, by zadne znaki stojace obok siebie nie powtarzaly sie.
"""

# Wersja 1
def usunPowtarzajacychSieSasiadowV1(napis):
    nowyNapis = ""
    ostatniUsunietyZnak = ""

    for i in range(len(napis) - 1):
        if not napis[i] == napis[i + 1]:
            nowyNapis += napis[i]
            ostatniUsunietyZnak = napis[i]

    if len(napis) and napis[-1] != ostatniUsunietyZnak:
        nowyNapis += napis[-1]

    return nowyNapis


# Testy Poprawnosci
napis = "AAAAAAAAAABBBBBBBBA"
wynik = "ABA"
assert usunPowtarzajacychSieSasiadowV1(napis) == wynik

napis = "XXXYYASFBY"
wynik = "XYASFBY"
assert usunPowtarzajacychSieSasiadowV1(napis) == wynik

napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC"
wynik = "C"
assert usunPowtarzajacychSieSasiadowV1(napis) == wynik

napis = ""
wynik = ""
assert usunPowtarzajacychSieSasiadowV1(napis) == wynik

napis = "AAABB"
wynik = "AB"
assert usunPowtarzajacychSieSasiadowV1(napis) == wynik
