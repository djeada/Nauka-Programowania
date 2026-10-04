r"""
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Wczytaj ścieżkę folderu i rozszerzenie (np. `.txt`). Wypisz nazwy wszystkich **plików** o tym rozszerzeniu, które leżą **bezpośrednio** w tym folderze. Nie zaglądaj do podfolderów. Foldery pomijaj, nawet jeśli ich nazwa wygląda jak nazwa pliku (np. folder `stare.txt`).

Rozszerzenia porównuj bez względu na wielkość liter, ale nazwy wypisuj dokładnie tak, jak są zapisane.

### Wejście

* 1. linia: ścieżka folderu
* 2. linia: rozszerzenie z kropką, np. `.txt`

### Wyjście

* Nazwy pasujących plików (same nazwy, bez ścieżki folderu), każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli w folderze nie ma żadnego pasującego pliku.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Przykład

**Pliki przed:**

```
dokumenty/lista zakupów.txt
| mleko
| chleb
dokumenty/notatki.TXT
| Zadzwonić do Ani.
dokumenty/zdjęcie.png
dokumenty/stare/archiwum.txt
```

**Wejście:**

```
dokumenty
.txt
```

**Wyjście:**

```
lista zakupów.txt
notatki.TXT
```

Plik `stare/archiwum.txt` leży w podfolderze, więc go pomijamy.

### Przykład 2

**Pliki przed:** *(brak)*

**Wejście:**

```
zdjecia
.png
```

**Wyjście:**

```
Folder nie istnieje.
```

### Uwagi

* Zawartość folderu zwraca `os.listdir()` albo `Path.iterdir()`. Rozszerzenie pliku poda `os.path.splitext()` albo `Path.suffix`.

"""

from pathlib import Path


def pliki_z_rozszerzeniem(folder, rozszerzenie):
    """Zwraca posortowane nazwy plików o danym rozszerzeniu leżących bezpośrednio w folderze."""
    nazwy = []
    for sciezka in Path(folder).iterdir():
        if sciezka.is_file() and sciezka.suffix.lower() == rozszerzenie.lower():
            nazwy.append(sciezka.name)
    return sorted(nazwy)


if __name__ == "__main__":
    folder = input()
    rozszerzenie = input()

    if not Path(folder).is_dir():
        print("Folder nie istnieje.")
    else:
        nazwy = pliki_z_rozszerzeniem(folder, rozszerzenie)
        if nazwy:
            print("\n".join(nazwy))
        else:
            print("Brak plików.")
