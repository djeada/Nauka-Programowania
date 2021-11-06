"""
Otrzymujesz napis reprezentujący zdanie. Znajdź najczęściej występującą literę 
w zdaniu. Jeśli więcej niż jedna litera występuje tą samą liczbę razy, zwróć 
literę najwcześniej pojawiającą się w zdaniu..
"""

def najczestsza_litera(napis):
    """
    Zwraca najczęściej występującą literę w napisie.
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