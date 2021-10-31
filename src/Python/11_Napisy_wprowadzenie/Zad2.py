"""
Dla otrzymanego napisu: oraz znaku, znajdź liczbę wystąpień znaku w napisie.
"""

def liczba_wystapien(napis, znak):
    return napis.count(znak)

def test_liczba_wystapien():
    assert liczba_wystapien("ala ma kota", "a") == 3
    assert liczba_wystapien("ala ma kota", "k") == 1


if __name__ == "__main__":

    test_liczba_wystapien()

