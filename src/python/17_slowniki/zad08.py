"""
Tytul: Najczesciej wystepujaca litera w zdaniu
Tresc: Otrzymujesz napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie najczesciej wystepujacej litery w zdaniu. Jesli wiecej niz jedna litera wystepuje te sama liczbe razy, nalezy zwrocic litere najwczesniej pojawiajaca sie w zdaniu.
Dane wejsciowe: Napis.
Dane wyjsciowe: Znak.
Przyklad:
Dla otrzymanego napisu: "lezy jerzy na wiezy"
Powinna zostac zwrocona litera: 'e'

"""

def najczestsza_litera(napis):
    """
    Zwraca najczesciej wystepujaca litere w napisie.
    """
    slownik = {}
    for litera in napis:
        if litera in slownik:
            slownik[litera] += 1
        else:
            slownik[litera] = 1
    return max(slownik, key=slownik.get)

def test_najczestsza_litera():

    assert najczestsza_litera("ala ma kota") == "a"

if __name__ == "__main__":

    test_najczestsza_litera()

