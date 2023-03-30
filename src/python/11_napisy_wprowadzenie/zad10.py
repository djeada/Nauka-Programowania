"""
Tytul: Policz wystapienia znaku.
Tresc: Dla podanego napisu i znaku, znajdz liczbe wystapien tego znaku w napisie.
Dane wejsciowe: Napis oraz znak.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "klamra" oraz znaku 'a', powinno zostac zwrocone: 2.

"""
import string

def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()

def najdluzsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return max(slowa, key=len)

def najkrotsze_slowo(zdanie):
    slowa = podziel_zdanie_na_slowa(zdanie)
    return min(slowa, key=len)

def test_najdluzsze_slowo():
    assert najdluzsze_slowo("Ala ma kota.") == "kota"

def test_najkrotsze_slowo():
    assert najkrotsze_slowo("Ala ma kota.") == "ma"

if __name__ == "__main__":

    test_najdluzsze_slowo()
    test_najkrotsze_slowo()

