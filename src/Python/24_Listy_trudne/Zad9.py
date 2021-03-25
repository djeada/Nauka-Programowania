"""
Znajdz najdluzszy naprzemienny podciag.
"""

# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(1)
def najdluzszyNaprzemiennyPodciagV1(lista):

    dlugoscMaks = 1
    indeksKoncowy = 0
    dlugosc = 1

    for i in range(len(lista) - 1):

        if lista[i] * lista[i + 1] < 0:

            dlugosc += 1

            if dlugosc > dlugoscMaks:
                dlugoscMaks = dlugosc
                indeksKoncowy = i + 1

        else:
            dlugosc = 1

    return lista[indeksKoncowy - dlugoscMaks + 1 : indeksKoncowy + 1]


if __name__ == "__main__":

    A = [1, -2, 6, 4, -3, 2, -4, -3]
    print(najdluzszyNaprzemiennyPodciagV1(A))
