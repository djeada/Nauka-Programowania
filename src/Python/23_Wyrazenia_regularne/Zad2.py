"""
Sprawdz czy haslo spelnia nastepujace warunki:
1. Przynajmniej jedna mala litera [a-z]
2. przynajmniej jedna duza litera [A-Z]
3. Przynajmniej jedna cyfra [0-9]
4. Prynajmniej jeden znak specjalny [!$#@_]
5. Minimalna dlugosc: 8
6. Maksymalna dlugosc: 15
"""

import re

# Wersja 1
def sprawdzPoprawnoscV1(haslo):
    if re.search("[a-z]", haslo) and re.search("[A-Z]", haslo):
        if re.search("[0-9]", haslo) and re.search("[!$#@_]", haslo):
            return len(haslo) >= 8 and len(haslo) <= 15

    return False


# Testy Poprawnosci
hasla = ["123456", "HulaKula123!", "$$KAsiORA302$$", "proste_haslo123", "22tajnE!"]
wyniki = [False, True, True, False, True]

for haslo, wynik in zip(hasla, wyniki):
    assert sprawdzPoprawnoscV1(haslo) == wynik
