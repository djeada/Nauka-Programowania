"""
Dla otrzymanych dwoch napisow, znajdz i usun w pierwszym z nich wystapienia
drugiego.
"""

# Wersja 1
def usun_wszystkie_v1(zdanie, slowo):
    return zdanie.replace(slowo, "")


# Testy Poprawnosci
def test_1():
    zdanie = "Lezy jezy na wiezy"
    slowo = "zy"
    wynik = "Le je na wie"

    assert usun_wszystkie_v1(zdanie, slowo) == wynik


def main():
    test_1()


if __name__ == "__main__":
    main()
