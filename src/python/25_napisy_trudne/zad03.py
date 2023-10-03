"""
Tytul: Czy napis A jest poczatkiem napisu B?
Tresc: Dostajesz dwa napisy. Twoim zadaniem jest sprawdzenie, czy drugi napis zaczyna sie od pierwszego napisu.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisow: “Dinozaur jest zly” oraz “Dino”, zwrocona wartosc powinna byc: Prawda.

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
