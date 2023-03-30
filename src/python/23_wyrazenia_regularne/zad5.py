"""
Tytul: Podziel tekst wzgledem znakow interpunkcyjnych.
Tresc: Dostajesz napis. Podziel go wzgledem znakow interpunkcyjnych i zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu otrzymanych napisow.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisu: “Ani nie poszedl do kina, ani nie wybral sie do teatru.”, powinna zostac zwrocona lista: [“Ani nie poszedl do kina”, “ani nie wybral sie do teatru”].

"""

import re

def odfiltruj_cyfry(slowo):
    return re.sub("[^\d]", "", slowo)

def test_odfiltruj_cyfry():
    assert odfiltruj_cyfry("numer 32.19 wyzej niz 31.17") == "32193117"

if __name__ == "__main__":
    test_odfiltruj_cyfry()

