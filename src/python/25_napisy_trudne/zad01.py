"""
Tytul: Podmiana slowa w zdaniu.
Tresc: Masz trzy napisy: zdanie, slowo A i slowo B. Twoim zadaniem jest zamiana wszystkich wystapien slowa A na slowo B w zdaniu.
Dane wejsciowe: Trzy napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy”, “zy” oraz “rzy”, zwrocony napis powinien brzmiec: “Lerzy jerzy na wierzy”.

"""

# Wersja 1
def zamien_wszystkoV1(zdanie, napis_a, napis_b):
    return zdanie.replace(napis_a, napis_b)


# Testy Poprawnosci
def test_1():
    zdanie = "Lezy jezy na wiezy"
    napis_a = "zy"
    napis_b = "rzy"
    wynik = "Lerzy jerzy na wierzy"

    assert zamien_wszystkoV1(zdanie, napis_a, napis_b) == wynik


def main():
    test_1()


if __name__ == "__main__":
    main()
