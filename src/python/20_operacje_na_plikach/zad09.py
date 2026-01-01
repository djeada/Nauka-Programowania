"""
ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Otrzymujesz ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze **> 10240 bajtów** w tym folderze i jego podfolderach.

### Wejście

* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\DoUsunięcia
```

**Wyjście:**
*(brak)*

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
