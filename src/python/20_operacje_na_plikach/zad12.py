"""
Tytul: Przesun wszystkie pliki CSV do jednego folderu.
Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Przenies wszystkie pliki CSV z pierwszego folderu (oraz jego podfolderow) do drugiego folderu.
Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
Dane wyjsciowe: Brak.

"""

import pathlib


def przenies_pliki_csv(folder_1, folder_2):
    """
    Funkcja przenosi pliki csv z folderu folder_1 do folderu folder_2.
    """
    for plik in pathlib.Path(folder_1).glob("**/*.csv"):
        plik.rename(pathlib.Path(folder_2) / plik.name)


def test_przenies_pliki_csv():

    # stworz foldery testowe
    folder_1 = pathlib.Path("test_1")
    folder_1.mkdir(parents=True, exist_ok=True)
    folder_2 = pathlib.Path("test_2")
    folder_2.mkdir(parents=True, exist_ok=True)

    # stworz pliki testowe
    plik_1 = folder_1 / "plik_1.csv"
    plik_1.touch()
    plik_2 = folder_1 / "plik_2.csv"
    plik_2.touch()

    # przenies pliki
    przenies_pliki_csv(folder_1, folder_2)

    # sprawdz czy pliki zostaly przeniesione
    assert pathlib.Path(folder_2 / "plik_1.csv").exists()
    assert pathlib.Path(folder_2 / "plik_2.csv").exists()
    assert not pathlib.Path(folder_1 / "plik_1.csv").exists()
    assert not pathlib.Path(folder_1 / "plik_2.csv").exists()

    # usun foldery testowe
    import shutil

    shutil.rmtree("test_1")


if __name__ == "__main__":

    test_przenies_pliki_csv()
