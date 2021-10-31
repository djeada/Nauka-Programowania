"""
Otrzymujesz napis reprezentujacy zdanie. Usun spacje ze zdania.
"""


def usun_spacje(zdanie):
    return zdanie.replace(" ", "")


def test_usun_spacje():
    assert usun_spacje("Ala ma kota") == "Alamakota"


if __name__ == "__main__":

    test_usun_spacje()
