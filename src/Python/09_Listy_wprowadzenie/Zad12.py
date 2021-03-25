"""
Przesun elementy listy w danym kierunku (lewo, badz prawo).
Dla przesuwania w prawo pierwszy element trafia na miejsce drugiego, drugi trzeciego, a ostatni na miejsce pierwszego.

Wejscie:

- Lista n-elementowa.
- Kierunek rotacji.
- Liczba przescuniec.

Wyjscie:

- Zmodyfikowana lista wejsciowa.
"""

# Wersja 1
# Zlozonosc czasowa O(n)
# Zlozonosc pamieciowa O(n)
def rotacjaV1(lista, kierunek, liczba):

    if kierunek == "prawo":
        liczba *= -1

    return lista[liczba:] + lista[:liczba]


# Testy Poprawnosci
lista = [5, 27, 6, 2, 1, 10, 8]
kierunek = "lewo"
liczba = 2
wynik = [6, 2, 1, 10, 8, 5, 27]

assert rotacjaV1(lista, kierunek, liczba) == wynik

lista = [9, 9, 42, 47, 5, 6, 19, 7]
kierunek = "prawo"
liczba = 3
wynik = [6, 19, 7, 9, 9, 42, 47, 5]

assert rotacjaV1(lista, kierunek, liczba) == wynik
