"""
Tytul: Zbior potegowy
Tresc: Otrzymujesz liste liczb naturalnych. Zwroc zbior potegowy otrzymanej listy, czyli zbior wszystkich jej podzbiorow.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Lista list zawierajaca elementy z wejsciowej listy lub pusta liste.
Przyklad:
Dla wejsciowej listy [1, 2, 1], powinna zostac zwrocona lista: [[], [1], [2], [1, 2], [1, 1], [1, 2, 1]].

"""

# Zlozonosc O(n.2^n)
def zbior_potegowy(lista):
    # wymaga sortowania O(nlogn)
    lista.sort()

    N = int(pow(2, len(lista)))
    zbior_potegowy = set()

    for i in range(N):
        subset = [lista[j] for j in range(len(lista)) if i & (1 << j)]
        zbior_potegowy.add(tuple(subset))

    return zbior_potegowy

# Testy Poprawnosci
def test_1():
    lista = [1, 2, 1]
    wynik = {(1, 2), (1,), (2,), (1, 1, 2), (), (1, 1)}

    assert sorted(zbior_potegowy(lista)) == sorted(wynik)

def test_2():
    lista = [5, 3]
    wynik = {(), (3,), (3, 5), (5,)}

    assert sorted(zbior_potegowy(lista)) == sorted(wynik)

def test_3():
    lista = []
    wynik = {()}

    assert zbior_potegowy(lista) == wynik

def main():
    test_1()
    test_2()
    test_3()

if __name__ == "__main__":
    main()

