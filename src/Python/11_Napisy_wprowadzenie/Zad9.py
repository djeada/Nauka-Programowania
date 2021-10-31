"""
Otrzymujesz rekord z bazy danych reprezentujacy dane pracownika. Sa to kolejno: 
imie, nazwisko, miejsce urodzenia, stanowisko i zarobki. Informacje rozdzielone 
sa srednikami. Zapisz je w osobnych zmiennych i wypisz wraz z komunikatem.
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
