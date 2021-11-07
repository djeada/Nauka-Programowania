"""
Otrzymujesz napis reprezentujacy sciezke. 
a) Sprawdz, czy jest to sciezka pliku.
b) Sprawdz, czy jest to sciezka folderu.
"""

import pathlib


def czy_sciezka_pliku(sciezka):
    """
    Funkcja zwraca True jesli podana sciezka jest sciezka pliku,
    False w przeciwnym wypadku.
    """
    return pathlib.Path(sciezka).is_file()


def czy_sciezka_folderu(sciezka):
    """
    Funkcja zwraca True jesli podana sciezka jest sciezka folderu,
    False w przeciwnym wypadku.
    """
    return pathlib.Path(sciezka).is_dir()


def test_czy_sciezka_pliku():
    # stworz folder testowy
    pathlib.Path("test").mkdir()

    # stworz plik testowy
    pathlib.Path("test/test.txt").touch()

    assert czy_sciezka_pliku("test/test.txt")
    assert not czy_sciezka_pliku("test")

    # usun folder testowy
    import shutil

    shutil.rmtree("test", ignore_errors=True)


def test_czy_sciezka_folderu():
    # stworz folder testowy
    pathlib.Path("test").mkdir()

    assert czy_sciezka_folderu("test")

    # usun folder testowy
    import shutil

    shutil.rmtree("test", ignore_errors=True)


if __name__ == "__main__":
    test_czy_sciezka_pliku()
