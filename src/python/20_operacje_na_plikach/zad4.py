"""
Tytul: Dodaj wiersz do pliku.
Tresc zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke do pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany wiersz na poczatek pliku tekstowego.
Dane wejsciowe: Dwa napisy - sciezka do pliku oraz wiersz tekstu.
Dane wyjsciowe: Brak.

"""
import pathlib

def wypisz_plik(sciezka):

    plik = pathlib.Path(sciezka)
    if plik.is_file():
        print(plik.read_text())

if __name__ == "__main__":

    # stworz folder testowy
    pathlib.Path("test").mkdir()

    # stworz plik tekstowy
    plik = pathlib.Path("test/test.txt")
    plik.write_text("przykladowy tekst.\n")

    # wypisz tresc pliku
    wypisz_plik("test/test.txt")

    # usun folder testowy
    import shutil

    shutil.rmtree("test")

