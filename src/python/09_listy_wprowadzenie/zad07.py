"""
Tytul: Liczba mniejsza od najwiekszej i wieksza od wszystkich pozostalych.
Tresc: Otrzymujesz liste liczb naturalnych. Znajdz najwieksza i druga co do wielkosci liczbe w liscie, a nastepnie oblicz srednia arytmetyczna tych dwoch liczb i zwroc ja jako liczbe zmiennoprzecinkowa.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Liczba zmiennoprzecinkowa oznaczajaca srednia arytmetyczna najwiekszej i drugiej co do wielkosci liczby z listy.
Przyklad:
Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostac zwrocona liczba 8.0.

"""

def srednia_dwoch_najwiekszych(lista):

    if len(lista) < 2:
        return 0.00

    najwieksza = max(lista)
    najwieksza_druga = max(lista[: lista.index(najwieksza)])
    srednia = (najwieksza + najwieksza_druga) / 2
    return srednia

def test_srednia_dwoch_najwiekszych():

    assert srednia_dwoch_najwiekszych([]) == 0.00
    assert srednia_dwoch_najwiekszych([1]) == 0.00
    assert srednia_dwoch_najwiekszych([1, 2]) == 1.50
    assert srednia_dwoch_najwiekszych([3, 5, -7, 4, 9, -11, 2]) == 7.00
    assert (
        srednia_dwoch_najwiekszych([3, -2, 4, 9, -3, -40, 8, 5, -7, 4, 9, -11, 2])
        == 6.5
    )

if __name__ == "__main__":

    test_srednia_dwoch_najwiekszych()

