"""
Otrzymujesz napis reprezentujacy zdanie. Znajdz najczesciej wystepujaca litere 
w zdaniu. Jesli wiecej niz jedna litera wystepuje ta sama liczbe razy, zwroc 
litere najwczesniej pojawiajaca sie w zdaniu..
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
