"""
Tytul: Napis skladajacy sie z liczb od 1 do n.
Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb naturalnych od 1 do n.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".

"""

def liczby(n):
    napis = ""
    for i in range(1, n + 1):
        napis += str(i) + ", "
    return napis[:-2]

def test_liczby():
    assert liczby(-1) == ""
    assert liczby(5) == "1, 2, 3, 4, 5"

if __name__ == "__main__":

    test_liczby()

