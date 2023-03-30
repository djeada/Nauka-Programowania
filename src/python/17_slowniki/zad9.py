"""
Tytul: Czy slowniki sa identyczne?
Otrzymujesz dwa slowniki skladajace sie z par napisow i list liczb calkowitych. Listy sa nieuporzadkowane. Twoim zadaniem jest sprawdzenie, czy slowniki skladaja sie z tych samych par. Dwie listy uznajemy za identyczne, jesli zawieraja te same elementy, niezaleznie od kolejnosci, w jakiej sie one znajduja.
Dane wejsciowe: Dwa slowniki par: napis, lista liczb calkowitych.
Dane wyjsciowe: Wartosc boolowska.
Przyklad:
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4]}
Powinna zostac zwrocona wartosc logiczna: Prawda.
Dla otrzymanych slownikow:
{'a': [1, 2, 3], 'b': [4, 5]}, {'a': [3, 2, 1], 'b': [5, 4], 'c': [6, 7]}
Powinna zostac zwrocona wartosc logiczna: Falsz.

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

