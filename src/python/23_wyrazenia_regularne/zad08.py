"""
Tytul: Cyfry w slowach.
Tresc: Dostajesz napis reprezentujacy zdanie. Zapisz w liscie cyfry, ktore sa czescia slow. Cyfry oddzielone od liter spacja powinny zostac pominiete.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu: "Jerzy29 i An37a s3luchali91 lekcji 22 z jezyka polskiego", powinna zostac zwrocona lista: ["29", "37", "3891", "3"].

"""

import re


def cyfry_w_slowach(tekst):
    """
    Funkcja zwraca liste cyfr w slowach w tekscie.
    """
    return [
        re.sub("[^\d]", "", e) for e in tekst.split() if re.search(r"\B[0-9]+\B", e)
    ]


def test_cyfry_w_slowach():
    assert cyfry_w_slowach("jerzy29 i an37a s3uc8ali91 lekcji jezyka polki3go") == [
        "29",
        "37",
        "3891",
        "3",
    ]


if __name__ == "__main__":
    test_cyfry_w_slowach()
