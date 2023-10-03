"""
Tytul: Sortowanie przez scalanie.
Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania przez scalanie.
1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
2. Podziel liste na dwie rowne (lub prawie rowne) czesci.
3. Wywolaj rekurencyjnie sortowanie przez scalanie dla obu czesci listy.
4. Scal obie posortowane czesci listy w jedna posortowana liste.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

"""

# Zlozonosc czasowa O(n^2)
def sortuj_v1(tablica):
    def scalaj(tablica_a, tablica_b):
        wynik = list()

        while len(tablica_a) + len(tablica_b) > 0:

            if len(tablica_b) == 0 or (
                len(tablica_a) > 0 and tablica_a[0] < tablica_b[0]
            ):
                wynik.append(tablica_a[0])
                tablica_a = tablica_a[1:]

            else:
                wynik.append(tablica_b[0])
                tablica_b = tablica_b[1:]

        return wynik

    n = len(tablica)

    if n < 2:
        return tablica

    return scalaj(sortuj_v1(tablica[: n // 2]), sortuj_v1(tablica[n // 2 :]))


# Zlozonosc czasowa O(nlogn)
def sortuj_v2(tablica):
    def scalaj(tablica_a, tablica_b):
        wynik = list()
        indeks_a = indeks_b = 0

        while len(tablica_a) + len(tablica_b) > indeks_a + indeks_b:

            if len(tablica_b) <= indeks_b or (
                len(tablica_a) > indeks_a and tablica_a[indeks_a] < tablica_b[indeks_b]
            ):
                wynik.append(tablica_a[indeks_a])
                indeks_a += 1

            else:
                wynik.append(tablica_b[indeks_b])
                indeks_b += 1

        return wynik

    n = len(tablica)

    if n < 2:
        return tablica

    return scalaj(sortuj_v2(tablica[: n // 2]), sortuj_v2(tablica[n // 2 :]))


# Testy Poprawnosci
def test_1():
    tablica = [4, 2, 5, 3, 1]
    wynik = [1, 2, 3, 4, 5]

    assert sortuj_v1(tablica) == wynik


def test_2():
    tablica = [6, 5, 1, 2, 3, 1, 4, 3, 5, 2, 3]
    wynik = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

    assert sortuj_v1(tablica) == wynik


def test_3():
    tablica = [4, 2, 5, 3, 1]
    wynik = [1, 2, 3, 4, 5]

    assert sortuj_v2(tablica) == wynik


def test_4():
    tablica = [6, 5, 1, 2, 3, 1, 4, 3, 5, 2, 3]
    wynik = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

    assert sortuj_v2(tablica) == wynik


def main():
    test_1()
    test_2()
    test_3()
    test_4()


if __name__ == "__main__":
    main()
