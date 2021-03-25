"""
Znajdz zbior potegowy danego zbioru.
"""

# Zlozonosc O(n.2^n)
def zbiorPotegowy(lista):
    # wymaga sortowania O(nlogn)
    lista.sort()

    N = int(pow(2, len(lista)))
    zbiorPotegowy = set()

    for i in range(N):
        subset = [lista[j] for j in range(len(lista)) if i & (1 << j)]
        zbiorPotegowy.add(tuple(subset))

    return zbiorPotegowy


if __name__ == "__main__":

    lista = [1, 2, 1]
    wynik = {(1, 2), (1,), (2,), (1, 1, 2), (), (1, 1)}

    assert sorted(zbiorPotegowy(lista)) == sorted(wynik)
