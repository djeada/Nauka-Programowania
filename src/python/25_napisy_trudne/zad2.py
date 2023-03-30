"""
Tytul: Podmiana slowa w zdaniu.
Tresc: Masz trzy napisy: zdanie, slowo A i slowo B. Twoim zadaniem jest zamiana wszystkich wystapien slowa A na slowo B w zdaniu.
Dane wejsciowe: Trzy napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy”, “zy” oraz “rzy”, zwrocony napis powinien brzmiec: “Lerzy jerzy na wierzy”.

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

