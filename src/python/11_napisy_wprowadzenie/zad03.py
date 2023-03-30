"""
Tytul: Z ilu slow sklada sie zdanie?
Tresc: Zlicz, ile slow sklada sie z podanego zdania. Znaki interpunkcyjne nie sa brane pod uwage jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "gram na pianinie.", powinno zostac zwrocone: 3.

"""
import string

def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()

def liczba_slow_w_zdaniu(zdanie):
    return len(podziel_zdanie_na_slowa(zdanie))

def test_liczba_slow_w_zdaniu():
    assert liczba_slow_w_zdaniu("Ala ma kota.") == 3
    assert liczba_slow_w_zdaniu("Ala ma kota, a kot ma Ale.") == 7

if __name__ == "__main__":
    test_liczba_slow_w_zdaniu()

