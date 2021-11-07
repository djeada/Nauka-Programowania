"""
Otrzymujesz napis reprezentujacy sciezke pliku tekstowego. 
Wczytaj i wypisz tresc pliku.
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
