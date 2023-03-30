"""
Tytul: Zamien znaki na kody ASCII.
Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z otrzymanych numerow, oddzielonych przecinkami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Robot", powinien zostac zwrocony napis: "82, 111, 98, 111, 116".

"""
import string

def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()

def test_podziel_zdanie_na_slowa():
    assert podziel_zdanie_na_slowa("Ala ma kota.") == ["Ala", "ma", "kota"]

if __name__ == "__main__":

    test_podziel_zdanie_na_slowa()

