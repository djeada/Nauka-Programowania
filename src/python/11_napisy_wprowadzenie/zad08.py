"""
Tytul:Wypisz pionowo slowa, z ktorych sklada sie zdanie.
Tresc: Otrzymasz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe. Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Kilka napisow.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinno zostac wypisane: "Ala", "ma", "kota".

"""
import string

def podziel_zdanie_na_slowa(zdanie):
    return zdanie.translate(str.maketrans("", "", string.punctuation)).split()

def wypisz_pionowo(zdanie):
    for slowo in podziel_zdanie_na_slowa(zdanie):
        print(slowo)

if __name__ == "__main__":
    zdanie = "Ala ma kota, a kot ma Ale."
    wypisz_pionowo(zdanie)

