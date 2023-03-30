"""
Tytul: Nazwa pliku bez rozszerzenia.
Tresc: Otrzymujesz napis reprezentujacy sciezke pliku. Odfiltruj z niego nazwe pliku wraz z rozszerzeniem. Zwroc sama nazwe pliku bez rozszerzenia.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu "C:\my-long\path_directory\file.html", powinna zostac zwrocona nazwa pliku bez rozszerzenia "file".

"""

import re

def usun_z_wiersza(tekst, zakazane_slowo):
    """
    Funkcja usuwa z tekstu czesci wierszy zawierajace zakazane slowo,
    od wystapienia zakazanego slowa do konca.
    """
    return [re.sub(r"{0}.*".format(zakazane_slowo), "", e) for e in tekst.splitlines()]

def test_usun_z_wiersza():
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
    napis_a = "a"

    oczekiwane = [
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

    assert usun_z_wiersza(tekst, napis_a) == oczekiwane

if __name__ == "__main__":
    test_usun_z_wiersza()

