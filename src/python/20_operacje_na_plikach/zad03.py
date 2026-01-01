"""
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do znalezionych plików.

### Wejście

* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

**Wejście:**

```
raport.docx
```

**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów — program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

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
