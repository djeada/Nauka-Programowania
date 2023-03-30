"""
Tytul: Odwroc slowa w zdaniu.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zamien slowa zdania na te same napisy zapisane wspak. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "ala mak otak".

"""

def rozdziel_informacje(napis):
    lista = napis.split(";")
    return lista

def wypisz_informacje(napis):
    informacje = rozdziel_informacje(napis)
    print("Imie: {}".format(informacje[0]))
    print("Nazwisko: {}".format(informacje[1]))
    print("Miejsce urodzenia: {}".format(informacje[2]))
    print("Stanowisko: {}".format(informacje[3]))
    print("Zarobki: {}".format(informacje[4]))

if __name__ == "__main__":

    informacje = "Jan;Kowalski;Warszawa;kierownik;2000"
    wypisz_informacje(informacje)

