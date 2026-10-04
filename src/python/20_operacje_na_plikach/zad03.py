r"""
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Wczytaj ścieżkę folderu i nazwę pliku (np. `raport.txt`). Przeszukaj ten folder **i wszystkie jego podfoldery** (na dowolnej głębokości) i wypisz ścieżki wszystkich plików o dokładnie takiej nazwie.

* Nazwy porównuj dokładnie — wielkość liter ma znaczenie (`Raport.txt` to inna nazwa niż `raport.txt`).
* Wypisuj tylko pliki. Folder o szukanej nazwie nie jest wynikiem, ale jego wnętrze też przeszukaj.
* Ścieżki wypisuj względem podanego folderu. Folder `.` oznacza cały katalog roboczy.

### Wejście

* 1. linia: ścieżka folderu, w którym zaczynasz szukanie (`.` = cały katalog roboczy)
* 2. linia: nazwa pliku

### Wyjście

* Ścieżki znalezionych plików względem podanego folderu, każda w osobnej linii, posortowane rosnąco.
* `Nie znaleziono.` — jeśli nie ma żadnego pliku o tej nazwie.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Przykład

**Pliki przed:**

```
raport.txt
2023/raport.txt
2023/raport.docx
2023/styczeń/raport.txt
2024/Raport.txt
```

**Wejście:**

```
.
raport.txt
```

**Wyjście:**

```
2023/raport.txt
2023/styczeń/raport.txt
raport.txt
```

`2024/Raport.txt` ma inną nazwę (wielka litera), a `2023/raport.docx` — inne rozszerzenie.

### Przykład 2

**Pliki przed:**

```
raport.txt
2023/raport.txt
2023/raport.docx
2023/styczeń/raport.txt
2024/Raport.txt
```

**Wejście:**

```
2023
raport.txt
```

**Wyjście:**

```
raport.txt
styczeń/raport.txt
```

Ścieżki są podane względem folderu `2023`.

### Uwagi

* Wszystkie pliki w folderze i jego podfolderach zwraca `os.walk()` albo `Path.rglob("*")`.

"""

from pathlib import Path


def znajdz_pliki(folder, nazwa_pliku):
    """Zwraca posortowane ścieżki (względem folderu) plików o danej nazwie."""
    baza = Path(folder)
    sciezki = []
    for sciezka in baza.rglob("*"):
        if sciezka.is_file() and sciezka.name == nazwa_pliku:
            sciezki.append(sciezka.relative_to(baza).as_posix())
    return sorted(sciezki)


if __name__ == "__main__":
    folder = input()
    nazwa_pliku = input()

    if not Path(folder).is_dir():
        print("Folder nie istnieje.")
    else:
        sciezki = znajdz_pliki(folder, nazwa_pliku)
        if sciezki:
            print("\n".join(sciezki))
        else:
            print("Nie znaleziono.")
