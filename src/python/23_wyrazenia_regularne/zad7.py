"""
Tytul: Usun fragment napisu.
Tresc: Dostajesz dwa napisy. Pierwszy napis to tekst, a drugi to slowo, ktore nalezy usunac z tekstu. Jesli w tekscie znajduje sie slowo do usuniecia, usun cala czesc tekstu od slowa do konca. Zwroc zmodyfikowany tekst.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla podanych napisow:
> Turned it up should no valley cousin he.
Speaking numerous ask did horrible packages set.
Ashamed herself has distant can studied mrs.
Led therefore its middleton perpetual fulfilled provision frankness.
Small he drawn after among every three no.
All having but you edward genius though remark one.
Rooms oh fully taken by worse do.
Points afraid but may end law lasted.
Was out laughter raptures returned outweigh.
Luckily cheered colonel me do we attacks on highest enabled.
Tried law yet style child.
Bore of true of no be deal.
Frequently sufficient in be unaffected.
The furnished she concluded depending procuring concealed.
oraz slowa "a", powinien zostac zwrocony napis:
> Turned it up should no v
Spe
Ash
Led therefore its middleton perpetu
Sm
All h
Rooms oh fully t
Points
W
Luckily cheered colonel me do we
Tried l
Bore of true of no be de
Frequently sufficient in be un
The furnished she concluded depending procuring conce.

"""

import re


def podziel_zdanie(zdanie):
    return [elem for elem in re.split(r"[,.!?]", zdanie) if elem]


def test_podziel_zdanie():
    zdanie = "hej, pan slimak! tak to ja. chodzcie to zaspiewam wam."
    oczekiwane = ["hej", " pan slimak", " tak to ja", " chodzcie to zaspiewam wam"]
    assert podziel_zdanie(zdanie) == oczekiwane


if __name__ == "__main__":
    test_podziel_zdanie()

