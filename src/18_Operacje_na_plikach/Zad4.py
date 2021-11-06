"""
Otrzymujesz napis reprezentujący ścieżkę pliku tekstowego. 
Wczytaj i wypisz treść pliku.
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

    # wypisz treść pliku
    wypisz_plik("test/test.txt")

    # usuń folder testowy
    import shutil
    shutil.rmtree("test") 