"""
Tytul: Sortowanie wzgledem kluczy/wartosci
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.
Dane wejsciowe: Slownik par: napis, liczba calkowita.
Dane wyjsciowe: Lista par.
Przyklad:
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].

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

