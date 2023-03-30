"""
Tytul: Pierwsze wystapienie klucza.
Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna jako klucz. Znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.
Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.
Dane wyjsciowe: Liczba calkowita oznaczajaca indeks pierwszego wystapienia klucza w liscie.
Przyklad:
Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostac zwrocone 2.

"""


def policz_samchody(lista):
    licznik = 0
    pom = 0
    for samochod in lista:
        if samochod == "A":
            pom += 1
        elif samochod == "B":
            licznik += pom

    return licznik


def test_policz_samochody():
    assert policz_samchody(["A", "B", "A", "B", "B"]) == 5
    assert (
        policz_samchody(["A", "A", "A", "B", "B", "A", "B", "A", "B", "A", "A", "A"])
        == 15
    )


if __name__ == "__main__":

    test_policz_samochody()

