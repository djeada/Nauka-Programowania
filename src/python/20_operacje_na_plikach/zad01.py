"""
ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.

### Wejście

* 1 linia: `path` (napis — ścieżka)

### Wyjście

* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

**Wyjście:**

```
Prawda
```

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
