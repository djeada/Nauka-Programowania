"""
Tytul: Wczytaj, zmodyfikuj i wypisz.
Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie. Nastepnie:
a) Dodaj 1 do kazdego elementu listy.
b) Pomnoz kazdy element przez jego indeks w liscie (indeksy zaczynaja sie od 0).
c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.
Dla kazdego z powyzszych podpunktow wypisz zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
Dane wejsciowe: N oraz N liczb calkowitych.
Dane wyjsciowe: N liczb calkowitych.
Przyklad:
Dla N rownego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.

"""

def czy_trojkat(lista):
    xA, yA, xB, yB, xC, yC = lista

    a = ((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5
    b = ((xC - xB) ** 2 + (yC - yB) ** 2) ** 0.5
    c = ((xA - xC) ** 2 + (yA - yC) ** 2) ** 0.5

    if a + b > c and a + c > b and b + c > a:
        return True

    return False

def test_czy_trojkat():
    assert not czy_trojkat([1, 1, 1, 1, 1, 1])
    assert not czy_trojkat([0, 0, 2, -2, 5, -5])
    assert czy_trojkat([-2, 4, 7, 5, 8, -8])

if __name__ == "__main__":

    test_czy_trojkat()

