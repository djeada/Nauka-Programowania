"""
Tytul: Zlicz instancje klasy w programie.
Tresc: Opis zadania: Stworz klase Klasa, ktora bedzie zawierala funkcje statyczna, zwracajaca aktualna liczbe instancji tej klasy w programie. Nastepnie stworz kilka obiektow tej klasy i przetestuj dzialanie funkcji.
Dane wejsciowe: brak
Dane wyjsciowe: liczba naturalna, reprezentujaca liczbe instancji klasy w programie.

"""

class Klasa:
    liczba_instancji = 0

    def __init__(self):
        Klasa.liczba_instancji += 1

    def __del__(self):
        Klasa.liczba_instancji -= 1

if __name__ == "__main__":
    a = Klasa()
    b = Klasa()
    print(Klasa.liczba_instancji)
    del a
    del b
    print(Klasa.liczba_instancji)

