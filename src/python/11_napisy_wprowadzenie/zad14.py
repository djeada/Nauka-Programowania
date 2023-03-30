"""
Tytul: Zamien litery "a" na znaki zapytania.
Tresc: Otrzymasz napis. Zmien litery "a" na znaki zapytania.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Latarnik", powinien zostac zwrocony napis: "L?t?rnik".

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

