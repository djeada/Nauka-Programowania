"""
Usun czesc wiersza od pierwszego wystapienia napisu A do konca.
"""

import re

# Wersja 1
def usunZWierszaV1(tekst, napisA):
    return [re.sub(r"{0}.*".format(napisA), "", e) for e in tekst.splitlines()]


if __name__ == "__main__":

    # Testy Poprawnosci
    tekst = """Turned it up should no valley cousin he. 
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
"""
    napisA = "a"

    wynik = [
        "Turned it up should no v",
        "Spe",
        "Ash",
        "Led therefore its middleton perpetu",
        "Sm",
        "All h",
        "Rooms oh fully t",
        "Points ",
        "W",
        "Luckily cheered colonel me do we ",
        "Tried l",
        "Bore of true of no be de",
        "Frequently sufficient in be un",
        "The furnished she concluded depending procuring conce",
    ]

    assert usunZWierszaV1(tekst, napisA) == wynik
