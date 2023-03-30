"""
Tytul: Znalezienie w folderze wszystkich plikow z danym rozszerzeniem
Tresc: Otrzymujesz dwa napisy. Pierwszy napis to sciezka folderu, a drugi to rozszerzenie szukanych plikow. Znajdz w folderze wszystkie pliki o podanym rozszerzeniu i zapisz ich nazwy w liscie.
Dane wejsciowe: Dwa napisy
Dane wyjsciowe: Lista napisow

"""

import pathlib
import shutil

def skopiuj_pliki_png(sciezka_1, sciezka_2):
    """
    Funkcja kopiuje wszystkie pliki .png z folderu sciezka_1 do folderu sciezka_2.
    """

    folder_1 = pathlib.Path(sciezka_1)
    folder_2 = pathlib.Path(sciezka_2)

    for plik in folder_1.glob("**/*.png"):
        shutil.copy(str(plik), str(folder_2))

def test_skopiuj_pliki_png():

    # stworz foldery testowe
    pathlib.Path("test_1").mkdir(parents=True, exist_ok=True)
    pathlib.Path("test_2").mkdir(parents=True, exist_ok=True)

    # stworz pliki testowe
    pathlib.Path("test_1/test_1.png").touch()
    pathlib.Path("test_1/test_2.png").touch()

    # skopiuj pliki
    skopiuj_pliki_png("test_1", "test_2")

    # sprawdz czy pliki zostaly skopiowane
    assert pathlib.Path("test_2/test_1.png").exists()
    assert pathlib.Path("test_2/test_2.png").exists()
    assert pathlib.Path("test_1/test_1.png").exists()
    assert pathlib.Path("test_1/test_2.png").exists()

    # usun foldery testowe
    shutil.rmtree("test_1")
    shutil.rmtree("test_2")

if __name__ == "__main__":

    test_skopiuj_pliki_png()

