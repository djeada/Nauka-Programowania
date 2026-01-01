"""
ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.

### Wejście

* 1 linia: `file_path`

### Wyjście

* treść pliku (dokładnie taka jak w pliku)

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\wiadomość.txt
```

**Wyjście:**

```
Witaj! To jest przykładowa treść pliku tekstowego.
```

"""
import pathlib


def wypisz_plik(sciezka):

    plik = pathlib.Path(sciezka)
    if plik.is_file():
        print(plik.read_text())


if __name__ == "__main__":

    # stworz folder testowy
    pathlib.Path("test").mkdir()

    # stworz plik tekstowy
    plik = pathlib.Path("test/test.txt")
    plik.write_text("przykladowy tekst.\n")

    # wypisz tresc pliku
    wypisz_plik("test/test.txt")

    # usun folder testowy
    import shutil

    shutil.rmtree("test")
