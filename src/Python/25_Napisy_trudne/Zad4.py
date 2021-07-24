"""
Usuń powtórzenia z napisu. Dany znak może pojawić się jedynie raz w całym napisie.
"""

# Wersja 1
def usun_powtorzenia_v1(napis):
    nowy_napis = ""
    for znak in napis:
        if znak not in nowy_napis:
            nowy_napis += znak

    return nowy_napis


# Testy Poprawnosci
napis = "AAAAAAAAAABBBBBBBBA"
wynik = "AB"
assert usun_powtorzenia_v1(napis) == wynik

napis = "XXXYYASFBY"
wynik = "XYASFB"
assert usun_powtorzenia_v1(napis) == wynik

napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC"
wynik = "C"
assert usun_powtorzenia_v1(napis) == wynik

napis = ""
wynik = ""
assert usun_powtorzenia_v1(napis) == wynik

napis = "AAABBAABBABABABA"
wynik = "AB"
assert usun_powtorzenia_v1(napis) == wynik
