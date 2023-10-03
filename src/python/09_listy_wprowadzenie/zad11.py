"""
Tytul: Samochody jadace w przeciwnych kierunkach.
Tresc: Otrzymujesz liste zlozona wylacznie z liter 'A' i 'B', ktore odpowiadaja samochodom jadacym odpowiednio na wschod ('A') i zachod ('B'). Policz, ile razy samochody jadace w przeciwnych kierunkach mijaja sie.
Dane wejsciowe: Lista znakow odpowiadajacych samochodom jadacym na wschod ('A') i zachod ('B').
Dane wyjsciowe: Liczba naturalna oznaczajaca liczbe mijajacych sie samochodow.
Przyklad:
Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostac zwrocona liczba 5.

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
