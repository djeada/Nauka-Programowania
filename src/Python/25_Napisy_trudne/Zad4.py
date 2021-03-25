"""
Usuń powtórzenia z napisu. Dany znak może pojawić się jedynie raz w całym napisie.
"""

# Wersja 1
def usunPowtorzeniaV1(napis):
    nowyNapis = ""
    for znak in napis:
        if znak not in nowyNapis:
            nowyNapis += znak

    return nowyNapis


# Testy Poprawnosci
napis = "AAAAAAAAAABBBBBBBBA"
wynik = "AB"
assert usunPowtorzeniaV1(napis) == wynik

napis = "XXXYYASFBY"
wynik = "XYASFB"
assert usunPowtorzeniaV1(napis) == wynik

napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC"
wynik = "C"
assert usunPowtorzeniaV1(napis) == wynik

napis = ""
wynik = ""
assert usunPowtorzeniaV1(napis) == wynik

napis = "AAABBAABBABABABA"
wynik = "AB"
assert usunPowtorzeniaV1(napis) == wynik
