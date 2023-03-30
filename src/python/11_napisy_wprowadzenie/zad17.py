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

def znamien_na_napis(lista):
    napis = ""
    for liczba in lista:
        napis += str(liczba)
    return napis

def test_znamien_na_napis():
    assert znamien_na_napis([1, 2, 3, 4, 5]) == "12345"

if __name__ == "__main__":

    test_znamien_na_napis()

