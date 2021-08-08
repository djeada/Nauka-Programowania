"""
Wypisz liczbe instancji klasy w programie.
"""

# Wersja 1
class Klasa:
    liczba_instancji = 0

    def __init__(self):
        Klasa.liczba_instancji += 1

    def wyswietl():
        print("Aktualna liczba instancji: ", Klasa.liczba_instancji)

    wyswietl = staticmethod(wyswietl)


# Testy poprawnosci
N = 5
[Klasa() for i in range(N)]

assert Klasa.liczba_instancji == N
