"""
Wypisz na przemian elemnty pierwszej i drugiej listy. 
Warunek: listy majac byc rownej dlugosci.
Wynik: jedna lista skladajaca sie z elementow obu otrzymanych list.
"""

# Wersja 1
def polaczListyV1(listA, listaB):

    if len(listA) != len(listaB):
        return False

    wynik = []

    for i in range(len(listaA)):
        wynik.append(listaA[i])
        wynik.append(listaB[i])

    return wynik


# Wersja 2
def polaczListyV2(listA, listaB):

    if len(listA) != len(listaB):
        return False

    wynik = []

    for a, b in zip(listaA, listaB):
        wynik.append(a)
        wynik.append(b)

    return wynik


# Testy Poprawnosci
listaA = ["a", "c", "e"]
listaB = ["b", "d", "f"]
wynik = ["a", "b", "c", "d", "e", "f"]

assert polaczListyV1(listaA, listaB) == wynik
assert polaczListyV2(listaA, listaB) == wynik
