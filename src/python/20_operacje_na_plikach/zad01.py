r"""
ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Wczytaj ścieżkę i sprawdź, co się pod nią znajduje w katalogu roboczym. Wypisz:

* `plik` — jeśli ścieżka wskazuje istniejący plik,
* `folder` — jeśli ścieżka wskazuje istniejący folder,
* `brak` — jeśli pod tą ścieżką nic nie ma.

### Wejście

* 1. linia: ścieżka (względna, z `/` jako separatorem; może zawierać spacje)

### Wyjście

Jedno słowo: `plik`, `folder` albo `brak`.

### Przykład

**Pliki przed:**

```
dane/raport.txt
| Raport kwartalny
```

**Wejście:**

```
dane/raport.txt
```

**Wyjście:**

```
plik
```

### Przykład 2

**Pliki przed:**

```
dane/raport.txt
| Raport kwartalny
```

**Wejście:**

```
dane
```

**Wyjście:**

```
folder
```

### Przykład 3

**Pliki przed:**

```
dane/raport.txt
| Raport kwartalny
```

**Wejście:**

```
raport.txt
```

**Wyjście:**

```
brak
```

Plik `raport.txt` leży w folderze `dane`, a nie bezpośrednio w katalogu roboczym.

### Uwagi

* Przydatne funkcje: `os.path.isfile()` i `os.path.isdir()` albo metody `Path.is_file()` i `Path.is_dir()` z modułu `pathlib`.

"""

import os


def rodzaj_sciezki(sciezka):
    """Zwraca 'plik', 'folder' albo 'brak' w zależności od tego, co jest pod ścieżką."""
    if os.path.isfile(sciezka):
        return "plik"
    if os.path.isdir(sciezka):
        return "folder"
    return "brak"


if __name__ == "__main__":
    sciezka = input()
    print(rodzaj_sciezki(sciezka))
