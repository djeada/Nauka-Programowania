"""
Otrzymujesz trzy napisy. Pierwszy napis reprezentuje zdanie. Drugi reprezentuje
slowo A wystepujace w zdaniu. Trzeci reprezentuje slowo B, na ktore ma zostac
zamienione slowo A. Podmien w zdaniu wszystkie wystapienia slowa A na slowo B.
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
