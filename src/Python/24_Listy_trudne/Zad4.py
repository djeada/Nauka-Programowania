"""
Otrzymujesz dwie listy binarne, A oraz B. 
Znajdz dlugosc takich podciagow obu list o rownej sumie, ktorych suma jest najwieksza.
Podciagi nie musza byc takie same.
"""

# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(n)
def znajdzPodciagV1(listaA, listaB):

    if len(listaA) != len(listaB):
        return False

    histo = {}

    histo[0] = -1

    wynik, sumaA, sumaB = 0, 0, 0

    for i in range(len(listaA)):

        sumaA += listaA[i]
        sumaB += listaB[i]

        roznica = sumaA - sumaB

        if roznica not in histo:
            histo[roznica] = i

        else:
            wynik = max(wynik, i - histo[roznica])

    return wynik


if __name__ == "__main__":

    # Testy poprawnosci
    listaA = [0, 0, 1, 1, 1, 1]
    listaB = [0, 1, 1, 0, 1, 0]
    wynik = 5

    print(znajdzPodciagV1(listaA, listaB))
