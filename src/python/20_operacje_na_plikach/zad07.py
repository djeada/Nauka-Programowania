"""
ZAD-07 — Dodaj wiersz na początku pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `write`, `prepend`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego i wiersz tekstu. Dodaj ten wiersz na **początku** pliku.

### Wejście

* 1 linia: `file_path`
* 2 linia: `line_to_add` (może zawierać spacje)

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

**Wyjście:**
*(brak)*

"""

import pathlib


def dostaw_wiersz(sciezka, wiersz):
    """
    Funkcja dostawia wiersz na poczatek pliku tekstowego.
    """
    with open(sciezka, "r") as plik:
        linie = plik.readlines()
    with open(sciezka, "w") as plik:
        plik.write(wiersz + "\n")
        for linia in linie:
            plik.write(linia)


def test_dostaw_wiersz():

    # stworz folder testowy
    pathlib.Path("test").mkdir(parents=True, exist_ok=True)

    # utworz plik testowy
    sciezka = "test/test.txt"
    pathlib.Path(sciezka).touch()
    pathlib.Path(sciezka).write_text("test 1\n")

    # dostaw wiersz na poczatek pliku
    wiersz = "test 2"
    dostaw_wiersz(sciezka, wiersz)

    # sprawdz czy plik zawiera wiersz
    assert pathlib.Path(sciezka).read_text().splitlines()[0] == wiersz

    # usun folder testowy
    import shutil

    shutil.rmtree("test")


if __name__ == "__main__":

    test_dostaw_wiersz()
