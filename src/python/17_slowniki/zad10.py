"""
Tytul: Slownik z kluczami bedacymi elementami jednej listy i wartosciami elementami drugiej listy.
Tresc: Dostajesz dwie listy liczb calkowitych. Stworz slownik, w ktorym kluczami beda elementy pierwszej listy, a wartosciami elementy drugiej listy. Jesli listy sa roznej dlugosci, zwroc pusty slownik.
Dane wejsciowe: Dwie listy liczb calkowitych.
Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami calkowitymi.
Przyklad:
Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], slownik powinien wygladac nastepujaco: {3: 1, 5: 2, 8: -1}.

"""

import string


def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja zwraca liste slow ze zdania.
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()


def na_male_litery(slowa):
    """
    Funkcja zamienia wielkie litery ze slow z listy slowa na male litery.
    """
    return [slowo.lower() for slowo in slowa]


def histogram(napis):
    """
    Funkcja zwraca slownik zawierajacy wszystkie litery w napisie oraz czestosc ich wystepowania.
    """
    histogram = {}
    for znak in napis:
        if znak in histogram:
            histogram[znak] += 1
        else:
            histogram[znak] = 1
    return histogram


def znajdz_wszystkie_anagramy_w_tekscie(napis):
    """
    Funkcja zwraca liste wszystkich anagramow w napisie.
    """
    slowa = podziel_zdanie_na_slowa(napis)
    slowa = na_male_litery(slowa)
    slowa = list(set(slowa))

    wynik = []
    i = 0
    while i < len(slowa):
        slowo = slowa[i]
        histogram_dla_slowa = histogram(slowo)
        wynik.append([slowo])
        slowa.remove(slowo)
        j = 0
        while j < len(slowa):
            inne_slowo = slowa[j]
            if inne_slowo != slowo:
                histogram_dla_innego_slowa = histogram(inne_slowo)
                if histogram_dla_slowa == histogram_dla_innego_slowa:
                    wynik[-1].append(inne_slowo)

            j += 1

        if len(wynik[-1]) == 1:
            wynik.pop()

        i += 1

    return wynik


def czy_listy_list_rowne(lista_a, lista_b):
    """
    Funkcja zwraca True jesli lista_a i lista_b skladaja sie z list, ktore maja taka sama ilosc elementow i elementy w tych listach sa takie same.
    """
    _lista_a = [tuple(sorted(x)) for x in lista_a]
    _lista_b = [tuple(sorted(x)) for x in lista_b]

    return set(_lista_a) == set(_lista_b)


def test_znajdz_wszystkie_anagramy_w_tekscie():
    assert znajdz_wszystkie_anagramy_w_tekscie("Ala ma kota") == []
    assert czy_listy_list_rowne(
        znajdz_wszystkie_anagramy_w_tekscie(
            "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia, jak bandzior i jego arbuz."
        ),
        [
            ["absurd", "brudas"],
            ["tyran", "narty"],
            ["bandzior", "zbrodnia"],
            ["burza", "arbuz"],
            ["galeria", "alergia"],
        ],
    )


if __name__ == "__main__":

    test_znajdz_wszystkie_anagramy_w_tekscie()

