"""
Tytul: Powtarzajace sie znaki
Otrzymujesz napis. Twoim zadaniem jest znalezienie i zwrocenie wszystkich znakow, ktore wystepuja co najmniej 2 razy w ciagu.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "aaabbbccc"
Powinien zostac zwrocony napis: "abc"

"""

def znaki_powtarzajace_sie_wiecej_niz_raz(napis):
    """
    Funkcja zwraca liste znakow powtarzajacych sie wiecej niz raz.
    """
    znaki = []
    for znak in napis:
        if napis.count(znak) > 1:
            znaki.append(znak)
    return znaki

def test_znaki_powtarzajace_sie_wiecej_niz_raz():
    assert znaki_powtarzajace_sie_wiecej_niz_raz("ababab") == ["a", "b"]
    assert znaki_powtarzajace_sie_wiecej_niz_raz("abc") == []

if __name__ == "__main__":

    test_znaki_powtarzajace_sie_wiecej_niz_raz()

