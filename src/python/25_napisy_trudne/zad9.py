"""
Tytul: Najdluzszy wspolny przedrostek.
Tresc: Dostajesz liste napisow. Znajdz najdluzszy wspolny przedrostek dla wszystkich napisow na liscie.
Dane wejsciowe: Lista napisow.
Dane wyjsciowe: Napis.
Przyklad:
Dla listy ["Remolada", "Remux", "Remmy"] powinien zostac zwrocony napis "Rem".

"""

# Wersja 1
def najdluzszy_podnapis_v1(slowo_a, slowo_b):

    m = len(slowo_a)
    n = len(slowo_b)

    pom = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if slowo_a[i - 1] == slowo_b[j - 1]:
                pom[i][j] = pom[i - 1][j - 1] + 1
            else:
                pom[i][j] = 0

    wynik = ""
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pom[i][j] > len(wynik):
                wynik = slowo_a[(i - pom[i][j] + 1) - 1 : pom[i][j]]

    return wynik


# Testy Poprawnosci
def test_1():
    slowo_a = "abcdxyz"
    slowo_b = "xyzabcd"
    wynik = "abcd"
    assert najdluzszy_podnapis_v1(slowo_a, slowo_b) == wynik


def test_2():
    slowo_a = "hhaall"
    slowo_b = "hhaall"
    wynik = "hhaall"
    assert najdluzszy_podnapis_v1(slowo_a, slowo_b) == wynik


def test_3():
    slowo_a = ""
    slowo_b = ""
    wynik = ""
    assert najdluzszy_podnapis_v1(slowo_a, slowo_b) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()

