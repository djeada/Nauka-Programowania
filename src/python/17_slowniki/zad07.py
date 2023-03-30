"""
Tytul: Histogram slow w tekscie
Tresc: Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezc czestosc wystepowania kazdego ze slow w tekscie. Nalezy zignorowac roznice miedzy malymi i wielkimi literami. Pamietaj, ze slowa skladaja sie wylacznie z liter.
Dane wejsciowe: Napis.
Dane wyjsciowe: Slownik par: napis, liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now."
Powinien zostac zwrocony slownik:
{"here": 1, "a": 12, "tricksy": 4, "corpus": 5, "will": 6, "exist": 1, "very": 2, "strange": 1, "sometimes": 1, "cryptic": 1, "dumbfound": 1, "you": 2, "maybe": 1, "perhaps": 1, "bit": 1, "in": 1, "particular": 1, "since": 1, "my": 1, "not": 1, "match": 1, "the": 2, "pattern": 1, "expect": 1, "from": 2, "it": 2, "nor": 1, "look": 1, "like": 1, "fish": 1, "boat": 1, "sunflower": 1, "or": 3, "handsome": 1, "kitten": 1, "surprise": 1, "user": 1, "named": 1, "ami": 1, "tavory": 1, "this": 1, "be": 1, "fun": 1, "to": 1, "follow": 1, "year": 1, "month": 1, "minute": 1, "now": 1}

"""

import string

def podziel_zdanie_na_slowa(zdanie):
    """
    Funkcja zwraca liste slow ze zdania.
    """
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()

def na_male_litery(slowa):
    """
    Funkcja zamienia wielkie litery ze slow z listy slowa na male litery.
    """
    return [slowo.lower() for slowo in slowa]

def policz_wystapienia_slow(slowa):
    """
    Funkcja zwraca slownik, gdzie kluczami sa slowa, a wartoscia ich ilosc wystapien.
    """
    slowa_bez_powtorzen = set(slowa)
    wynik = {}
    for slowo in slowa_bez_powtorzen:
        wynik[slowo] = slowa.count(slowo)
    return wynik

def policz_slowa_w_zdaniu(zdanie):
    """
    Funkcja zwraca slownik, gdzie kluczami sa slowa, a wartoscia ich ilosc wystapien.
    """
    slowa = podziel_zdanie_na_slowa(zdanie)
    slowa = na_male_litery(slowa)
    return policz_wystapienia_slow(slowa)

def test_policz_slowa_w_zdaniu():
    assert policz_slowa_w_zdaniu("Ala ma kota") == {"ala": 1, "ma": 1, "kota": 1}
    assert policz_slowa_w_zdaniu(
        "Here,,,, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you EXPECT from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now."
    ) == {
        "here": 1,
        "a": 12,
        "tricksy": 4,
        "corpus": 5,
        "will": 6,
        "exist": 1,
        "very": 2,
        "strange": 1,
        "sometimes": 1,
        "cryptic": 1,
        "dumbfound": 1,
        "you": 2,
        "maybe": 1,
        "perhaps": 1,
        "bit": 1,
        "in": 1,
        "particular": 1,
        "since": 1,
        "my": 1,
        "not": 1,
        "match": 1,
        "the": 2,
        "pattern": 1,
        "expect": 1,
        "from": 2,
        "it": 2,
        "nor": 1,
        "look": 1,
        "like": 1,
        "fish": 1,
        "boat": 1,
        "sunflower": 1,
        "or": 3,
        "handsome": 1,
        "kitten": 1,
        "surprise": 1,
        "user": 1,
        "named": 1,
        "ami": 1,
        "tavory": 1,
        "this": 1,
        "be": 1,
        "fun": 1,
        "to": 1,
        "follow": 1,
        "year": 1,
        "month": 1,
        "minute": 1,
        "now": 1,
    }

if __name__ == "__main__":

    test_policz_slowa_w_zdaniu()

