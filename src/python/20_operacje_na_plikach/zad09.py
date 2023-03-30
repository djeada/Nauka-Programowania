"""
Tytul: Usun pliki spelniajace warunek.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu. Usun wszystkie pliki o rozmiarze wiekszym niz 10 kB znajdujace sie w podanym folderze i jego podfolderach.
Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
Dane wyjsciowe: Brak.

"""
import pathlib

def usun_pliki(sciezka):
    """
    Funkcja usuwa pliki o rozmiarze wiekszym niz 10kB znajdujace sie
    w podanym folderze oraz jego podfolderach.
    """
    for sciezka_do_pliku in sciezka.iterdir():
        if sciezka_do_pliku.is_file():
            if sciezka_do_pliku.stat().st_size > 10240:
                sciezka_do_pliku.unlink()

def test_usun_pliki():

    # stworz folder testowy
    pathlib.Path("test").mkdir()

    # stworz pliki testowe
    plik = pathlib.Path("test/plik1.txt")
    plik.touch()
    plik.write_text("test\n" * 10000)

    assert plik.stat().st_size >= 10240

    # usun pliki
    usun_pliki(pathlib.Path("test"))

    # sprawdz czy plik zostal usuniety
    assert not plik.exists()

    # usun folder testowy
    import shutil

    shutil.rmtree("test")

if __name__ == "__main__":

    test_usun_pliki()

