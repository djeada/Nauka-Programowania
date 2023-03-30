"""
Tytul: Sprawdz czy slowo wystepuje w zdaniu.
Tresc: Dostajesz dwa napisy. Sprawdz, czy drugi napis wystepuje w pierwszym jako pojedyncze slowo.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisow: “Siala baba mak.” oraz “babcia”, powinna zostac zwrocona wartosc logiczna: Falsz.

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

