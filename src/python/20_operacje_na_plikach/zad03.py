"""
Tytul: Znalezienie sciezki pliku o danej nazwie
Tresc: Otrzymujesz napis reprezentujacy nazwe pliku. Przeszukaj caly system i zapisz w liscie wszystkie sciezki plikow o podanej nazwie.
Dane wejsciowe: Napis
Dane wyjsciowe: Lista napisow

"""

import pathlib

def znajdz_sciezki(nazwa_pliku):
    """
    Funkcja zwraca liste sciezek do plikow o podanej nazwie.
    """
    sciezki = []
    for plik in pathlib.Path.home().glob("**/*"):
        if plik.name == nazwa_pliku:
            sciezki.append(str(plik.absolute()))
    return sciezki

def test_znajdz_sciezki():

    # stworz foldery testowe
    sciezka1 = "test"
    sciezka2 = "test/test1"
    sciezka3 = "test/test2"
    pathlib.Path(sciezka1).mkdir()
    pathlib.Path(sciezka2).mkdir()
    pathlib.Path(sciezka3).mkdir()

    # utworz pliki testowe
    nazwa_pliku = "test.txt"
    plik_1 = pathlib.Path(f"{sciezka1}/{nazwa_pliku}")
    plik_1.touch()
    plik_2 = pathlib.Path(f"{sciezka2}/{nazwa_pliku}")
    plik_2.touch()
    plik_3 = pathlib.Path(f"{sciezka3}/{nazwa_pliku}")
    plik_3.touch()

    wynik = znajdz_sciezki(nazwa_pliku)
    assert str(plik_1.absolute()) in wynik
    assert str(plik_2.absolute()) in wynik
    assert str(plik_3.absolute()) in wynik

    # usun foldery testowe
    import shutil

    shutil.rmtree(sciezka1)

if __name__ == "__main__":
    test_znajdz_sciezki()

