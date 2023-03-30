"""
Tytul: Plik z lista adresow IP.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Kazdy wiersz pliku reprezentuje adres IP. Posortuj adresy IP i zapisz je w liscie.
Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
Dane wyjsciowe: Lista adresow IP posortowanych alfabetycznie.

"""

import pathlib


def znajdz_pliki_z_rozszerzeniem(sciezka, rozszerzenie):
    """
    Funkcja zwraca liste plikow o podanym rozszerzeniu.
    """
    lista_plikow = []
    for plik in pathlib.Path(sciezka).glob("*." + rozszerzenie):
        lista_plikow.append(str(plik.relative_to(pathlib.Path(sciezka).parent)))
    return lista_plikow


def test_znajdz_pliki_z_rozszerzeniem():

    # stworz folder testowy
    sciezka_folderu = "test"
    pathlib.Path(sciezka_folderu).mkdir(parents=True, exist_ok=True)

    # stworz pliki testowe
    sciezka_pliku_1 = "test/plik.txt"
    sciezka_pliku_2 = "test/plik2.txt"
    pathlib.Path(sciezka_pliku_1).touch()
    pathlib.Path(sciezka_pliku_2).touch()

    assert set(
        map(pathlib.Path, znajdz_pliki_z_rozszerzeniem(sciezka_folderu, "txt"))
    ) == set(map(pathlib.Path, [sciezka_pliku_1, sciezka_pliku_2]))

    # usun folder testowy
    import shutil

    shutil.rmtree(sciezka_folderu)


if __name__ == "__main__":

    test_znajdz_pliki_z_rozszerzeniem()

