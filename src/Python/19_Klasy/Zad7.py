"""
Wypisz liczbę instancji klasy w programie.
"""

# Wersja 1
class Klasa:
    liczbaInstancji = 0

    def __init__(self):
        Klasa.liczbaInstancji += 1

    def wyswietl():
        print("Aktualna liczba instancji: ", Klasa.liczbaInstancji)

    wyswietl = staticmethod(wyswietl)


# Testy poprawnosci
N = 5
[Klasa() for i in range(N)]

assert Klasa.liczbaInstancji == N
