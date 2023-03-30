"""
Tytul: Czy srednia elementow znajduje sie w liscie?
Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako klucza, usun pierwsze wystapienie klucza w liscie.
Dane wejsciowe: Lista liczb calkowitych i liczba calkowita jako klucz.
Dane wyjsciowe: Lista liczb calkowitych bez pierwszego wystapienia klucza.
Przyklad:
Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].

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

