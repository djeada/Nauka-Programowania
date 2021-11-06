"""
Otrzymujesz napis. Znajdź w otrzymanym napisie wszystkie znaki 
powtarzające się więcej niż raz.
"""

def znaki_powtarzajace_sie_wiecej_niz_raz(napis):
    '''
    Funkcja zwraca listę znaków powtarzających się więcej niż raz.
    '''
    znaki = []
    for znak in napis:
        if napis.count(znak) > 1:
            znaki.append(znak)
    return znaki


def test_znaki_powtarzajace_sie_wiecej_niz_raz():
    assert znaki_powtarzajace_sie_wiecej_niz_raz('ababab') == ['a', 'b']
    assert znaki_powtarzajace_sie_wiecej_niz_raz('abc') == []

if __name__ == "__main__":

    test_znaki_powtarzajace_sie_wiecej_niz_raz() 