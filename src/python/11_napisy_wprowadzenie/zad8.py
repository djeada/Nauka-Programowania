"""
Tytul: Konwersja listy na napis
Tresc: Otrzymujesz liste liczb naturalnych. Zamie liste na napis.
Dane wejsciowe: Lista liczb naturalnych.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej listy: [2, 4, 7], powinien zostac zwrocony napis: “247”.

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

