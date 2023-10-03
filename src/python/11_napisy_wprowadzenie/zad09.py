"""
Tytul: Wczytaj i rozdziel informacje o pracowniku.
Tresc: Otrzymasz rekord z bazy danych reprezentujacy dane pracownika. Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje sa rozdzielone srednikami. Zapisz je w osobnych zmiennych i wypisz je razem z odpowiednimi komunikatami.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista napisow.
Przyklad:
Dla otrzymanego napisu:
"Jan; Kowalski; Warszawa; Programista; 1000;",
powinna zostac zwrocona lista:
["Imie: Jan", "Nazwisko: Kowalski", "Miejsce urodzenia: Warszawa", "Zawod: Programista", "Zarobki: 1000"].

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
