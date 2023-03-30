"""
Tytul: Znalezienie indeksu najmniejszego elementu w posortowanej i przesunietej w prawo liscie.
Tresc: Dla otrzymanej listy liczb calkowitych, znajdz indeks najmniejszego elementu. Lista jest posortowana rosnaco, ale zostala przesunieta w prawo o okreslona liczbe miejsc. Przykladowo dla przesuniecia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.
Dane wejsciowe: Lista liczb calkowitych oraz liczba naturalna okreslajaca przesuniecie w prawo.
Dane wyjsciowe: Liczba calkowita.
Przyklad:
Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrocona liczba: 2.

"""


def usun_duplikaty_v1(lista):
    lista_nowa = []
    for i in lista:
        if i not in lista_nowa:
            lista_nowa.append(i)
    return lista_nowa


def usun_duplikaty_v2(lista):
    return list(set(lista))


def test_usun_duplikaty_v1():
    assert usun_duplikaty_v1([]) == []
    assert usun_duplikaty_v1([1, 1, 1, 1, 1]) == [1]
    assert usun_duplikaty_v1([3, 5, 3, 3, 2]) == [3, 5, 2]


if __name__ == "__main__":

    test_usun_duplikaty_v1()

