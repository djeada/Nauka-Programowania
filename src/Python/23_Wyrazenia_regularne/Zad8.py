"""
Wyciagnij cyfry bedace czescia slow.
"""

import re

# Wersja 1
def cyfryWSlowachV1(tekst):
    return [
        re.sub("[^\d]", "", e) for e in tekst.split() if re.search(r"\B[0-9]+\B", e)
    ]


if __name__ == "__main__":

    # Testy Poprawnosci
    tekst = "jerzy29 i an37a s3uc8ali91 lekcji jezyka polki3go"
    wynik = ["29", "37", "3891", "3"]

    assert cyfryWSlowachV1(tekst) == wynik
