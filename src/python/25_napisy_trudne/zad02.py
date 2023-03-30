"""
Tytul: Usun podnapis.
Tresc: Dostajesz dwa napisy. Twoim zadaniem jest wyszukanie i usuniecie wszystkich wystapien drugiego napisu w pierwszym napisie.
Dane wejsciowe: Dwa napisy.
Dane wyjsciowe: Napis.
Przyklad:
Dla napisow: “Lezy jezy na wiezy” oraz “zy”, zwrocony napis powinien brzmiec: “Le je na wie”.

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

