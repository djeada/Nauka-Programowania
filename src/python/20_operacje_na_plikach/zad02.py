"""
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

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
