"""
Tytul: Wieza Hanoi.
Tresc: N krazkow o roznych srednicach ulozonych jest na jednym z trzech slupkow (A, B lub C). Na dole znajduje sie krazek o najwiekszej srednicy. Kazdy nastepny jest mniejszy od poprzedniego. Znajdz sposob na przelozenie wszystkich krazkow na inny slupek. Pamietaj, ze nie wolno klasc krazka o wiekszej srednicy na krazek o mniejszej srednicy, ani przekladac kilku krazkow jednoczesnie.
Dane wejsciowe: Liczba naturalna N.
Dane wyjsciowe: Lista par znakow.
Przyklad:
Dla N = 3, powinna zostac zwrocona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]

"""

def hanoi(n):
    """
    Funkcja zwraca liste ruchow, ktore powinny byc wykonane, aby
    przelozyc n krazkow ze slupka A na slupek B. Slupek C jest
    slupkiem pomocniczym.
    """

    def hanoi_rek(n, from_tower, to_tower, aux_tower, wynik):
        """
        Rekurencyjna funkcja wewnetrzna.
        """
        if n == 1:
            wynik.append((from_tower, to_tower))
        else:
            hanoi_rek(n - 1, from_tower, aux_tower, to_tower, wynik)
            hanoi_rek(1, from_tower, to_tower, aux_tower, wynik)
            hanoi_rek(n - 1, aux_tower, to_tower, from_tower, wynik)
        return wynik

    wynik = list()
    hanoi_rek(n, "A", "B", "C", wynik)
    return wynik

def test_hanoi():
    assert hanoi(1) == [("A", "B")]
    assert hanoi(2) == [("A", "C"), ("A", "B"), ("C", "B")]
    assert hanoi(3) == [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("A", "B"),
        ("C", "A"),
        ("C", "B"),
        ("A", "B"),
    ]

if __name__ == "__main__":
    test_hanoi()

