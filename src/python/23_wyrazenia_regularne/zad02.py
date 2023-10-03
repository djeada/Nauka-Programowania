"""
Tytul: Sprawdz poprawnosc hasla.
Tresc: Masz napis reprezentujacy haslo. Sprawdz, czy haslo spelnia nastepujace warunki:
1. Haslo musi zawierac przynajmniej jedna mala litere [a-z].
2. Haslo musi zawierac przynajmniej jedna duza litere [A-Z].
3. Haslo musi zawierac przynajmniej jedna cyfre [0-9].
4. Haslo musi zawierac przynajmniej jeden znak specjalny [! # $ % & ' * + — / = ? ^ _ ` { | } ~].
5. Minimalna dlugosc hasla to 8 znakow.
6. Maksymalna dlugosc hasla to 20 znakow.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisu: “abc1234”, powinna zostac zwrocona wartosc logiczna: Falsz.

"""

import re


def czy_haslo_poprawne(haslo):
    """
    Sprawdza czy haslo jest poprawne.
    """
    if len(haslo) < 8 or len(haslo) > 20:
        return False
    if re.search(r"[a-z]", haslo) is None:
        return False
    if re.search(r"[A-Z]", haslo) is None:
        return False
    if re.search(r"[0-9]", haslo) is None:
        return False
    if re.search(r"[! # $ % & \' * + - / = ? ^ _ ` { | } ~]", haslo) is None:
        return False
    return True


def test_czy_haslo_poprawne():
    assert not czy_haslo_poprawne("Ab1!")
    assert not czy_haslo_poprawne("haslo")
    assert not czy_haslo_poprawne("HASLO")
    assert not czy_haslo_poprawne("HASLO123!@#")
    assert not czy_haslo_poprawne("12345678")
    assert not czy_haslo_poprawne("proste_haslo")
    assert not czy_haslo_poprawne("Haslo123")
    assert czy_haslo_poprawne("Haslo123!")
    assert czy_haslo_poprawne("Haslo123!#")
    assert czy_haslo_poprawne("Haslo123!#$")
    assert czy_haslo_poprawne("Haslo123!#$%&*")


if __name__ == "__main__":
    test_czy_haslo_poprawne()
