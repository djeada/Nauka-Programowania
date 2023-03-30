"""
Tytul: Najdluzszy naprzemienny podciag.
Tresc: Masz dana liste liczb. Znajdz najdluzszy podciag naprzemienny w tej liscie. Ciag jest naprzemienny, jesli liczby w nim rosna i maleja na zmiane. Na przyklad [1, 3, 2, 4, 3, 5] jest naprzemienny.
Dane wejsciowe: Lista n liczb calkowitych.
Dane wyjsciowe: Lista liczb calkowitych reprezentujaca najdluzszy podciag naprzemienny w tej liscie.
Przyklad:
Dla listy liczb: [1, -2, 6, 4, -3, 2, -4, -3], powinna zostac zwrocona lista [1, -2, 6, -3, 2, -4].

"""

# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(1)
def najdluzszy_naprzemienny_podciag_v1(lista):

    dlugosc_maks = 1
    indeks_koncowy = 0
    dlugosc = 1

    for i in range(len(lista) - 1):

        if lista[i] * lista[i + 1] < 0:

            dlugosc += 1

            if dlugosc > dlugosc_maks:
                dlugosc_maks = dlugosc
                indeks_koncowy = i + 1

        else:
            dlugosc = 1

    wynik = lista[indeks_koncowy - dlugosc_maks + 1 : indeks_koncowy + 1]

    if len(wynik) > 1:
        return wynik

    return list()

# Testy Poprawnosci
def test_1():
    lista = [1, -2, 6, 4, -3, 2, -4, -3]
    wynik = [4, -3, 2, -4]

    assert najdluzszy_naprzemienny_podciag_v1(lista) == wynik

def test_2():
    lista = [1, 2, 3, 4, 5]
    wynik = []

    assert najdluzszy_naprzemienny_podciag_v1(lista) == wynik

def test_3():
    lista = []
    wynik = []

    assert najdluzszy_naprzemienny_podciag_v1(lista) == wynik

def main():
    test_1()
    test_2()
    test_3()

if __name__ == "__main__":
    main()

