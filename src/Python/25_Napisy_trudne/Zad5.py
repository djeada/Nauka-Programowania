"""
Zmodyfikuj napis w taki sposob, by zadne znaki stojace obok siebie nie powtarzaly sie.
"""

# Wersja 1
def usun_powtarzajacych_sie_sasiadow_v1(napis):
    nowy_napis = ""
    ostatni_usuniety_znak = ""

    for i in range(len(napis) - 1):
        if not napis[i] == napis[i + 1]:
            nowy_napis += napis[i]
            ostatni_usuniety_znak = napis[i]

    if len(napis) and napis[-1] != ostatni_usuniety_znak:
        nowy_napis += napis[-1]

    return nowy_napis


# Testy Poprawnosci
napis = "AAAAAAAAAABBBBBBBBA"
wynik = "ABA"
assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik

napis = "XXXYYASFBY"
wynik = "XYASFBY"
assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik

napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC"
wynik = "C"
assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik

napis = ""
wynik = ""
assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik

napis = "AAABB"
wynik = "AB"
assert usun_powtarzajacych_sie_sasiadow_v1(napis) == wynik
