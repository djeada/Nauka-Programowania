"""
Tytul: Znalezienie elementu bez pary w liscie liczb calkowitych.
Tresc: Dla otrzymanej listy liczb calkowitych, skladajacej sie z nieparzystej liczby elementow, znajdz element, ktory nie ma pary o tej samej wartosci.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy: [1, 3, 1, 7, 3, 1, 1] zostanie zwrocona liczba: 7.

"""


def element_bez_pary(lista):
    for i in lista:
        if lista.count(i) % 2 == 1:
            return i


def test_element_bez_pary():
    assert element_bez_pary([1, 3, 1, 7, 3, 1, 1]) == 7
    assert element_bez_pary([1, 1, 2, 2, 3, 4, 4, 5, 5]) == 3
    assert element_bez_pary([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 2]) == 2


if __name__ == "__main__":

    test_element_bez_pary()
