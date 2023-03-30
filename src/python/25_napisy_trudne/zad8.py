"""
Tytul: Powtarzajace sie podnapisy.
Tresc: Dostajesz napis. Znajdz wszystkie powtarzajace sie podnapisy w tym napisie.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla napisu "pythonpython" powinna zostac zwrocona lista zawierajaca napis "python".

"""

# Wersja 1
# Zlozonosc czasowa O(n^2)
def najdluzszy_przedrostek_v1(slowa):

    wynik = ""
    n = len(slowa)
    j = float("inf")

    for slowo in slowa:
        s = len(slowo)
        if j > s:
            j = s

    for i in range(j):
        pom = slowa[0][i]
        k = 1
        while k < n:
            if pom == slowa[k][i]:
                k += 1
            else:
                return wynik
        wynik += pom

    return wynik


# Testy Poprawnosci
def test_1():
    slowa = ["abcdefgh", "abcefgh", "abcd"]
    wynik = "abc"
    assert najdluzszy_przedrostek_v1(slowa) == wynik


def test_2():
    slowa = ["flower", "flow", "flight", "flix"]
    wynik = "fl"
    assert najdluzszy_przedrostek_v1(slowa) == wynik


def test_3():
    slowa = ["student", "studio", "stress", "lol"]
    wynik = ""
    assert najdluzszy_przedrostek_v1(slowa) == wynik


def main():
    test_1()
    test_2()
    test_3()


if __name__ == "__main__":
    main()

