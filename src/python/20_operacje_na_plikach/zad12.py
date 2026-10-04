r"""
ZAD-12 — Przenieś wszystkie pliki CSV do jednego folderu (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `move`, `csv`, `recursive`

### Treść

Wczytaj ścieżkę folderu źródłowego i docelowego. Przenieś wszystkie pliki z rozszerzeniem `.csv` (bez względu na wielkość liter) z folderu źródłowego **i wszystkich jego podfolderów** bezpośrednio do folderu docelowego, zachowując ich nazwy.

* Po przeniesieniu pliku nie ma już w starym miejscu. Foldery zostają, nawet jeśli staną się puste.
* Jeśli folder docelowy nie istnieje, utwórz go (razem z brakującymi folderami nadrzędnymi). Gdy nie ma czego przenosić, nie ma znaczenia, czy go utworzysz.

### Wejście

* 1. linia: ścieżka folderu źródłowego
* 2. linia: ścieżka folderu docelowego

### Wyjście

* Dawne ścieżki przeniesionych plików względem folderu źródłowego, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli nie ma żadnego pliku `.csv`.
* `Folder nie istnieje.` — jeśli folder źródłowy nie istnieje. Wtedy niczego nie twórz.

### Ograniczenia

* Nazwy plików `.csv` w całym folderze źródłowym są różne, a w folderze docelowym nie ma plików o takich nazwach.
* Folder docelowy nie leży wewnątrz folderu źródłowego.

### Przykład

**Pliki przed:**

```
projekt/dane.csv
| id,wartość
| 1,10
projekt/opis.txt
| Dane sprzedaży
projekt/2023/styczeń.csv
| 1,120
projekt/2023/q1/luty.CSV
| 2,95
```

**Wejście:**

```
projekt
wyniki/csv
```

**Wyjście:**

```
2023/q1/luty.CSV
2023/styczeń.csv
dane.csv
```

**Pliki po:**

```
wyniki/csv/dane.csv
| id,wartość
| 1,10
wyniki/csv/styczeń.csv
| 1,120
wyniki/csv/luty.CSV
| 2,95
projekt/dane.csv (usunięty)
projekt/2023/styczeń.csv (usunięty)
projekt/2023/q1/luty.CSV (usunięty)
projekt/opis.txt
| Dane sprzedaży
```

Program utworzył folder `wyniki/csv` i przeniósł do niego trzy pliki; `opis.txt` został na miejscu.

### Uwagi

* Plik przenosi `shutil.move(zrodlo, cel)` albo `Path.rename(cel)`.

"""

import shutil
from pathlib import Path


def przenies_pliki_csv(zrodlo, cel):
    """Przenosi pliki .csv z folderu zrodlo i jego podfolderów do folderu cel.

    Zwraca posortowane dawne ścieżki przeniesionych plików (względem folderu zrodlo).
    """
    baza = Path(zrodlo)
    folder_docelowy = Path(cel)
    folder_docelowy.mkdir(parents=True, exist_ok=True)

    pliki_csv = [
        sciezka
        for sciezka in baza.rglob("*")
        if sciezka.is_file() and sciezka.suffix.lower() == ".csv"
    ]
    przeniesione = []
    for sciezka in pliki_csv:
        shutil.move(str(sciezka), str(folder_docelowy / sciezka.name))
        przeniesione.append(sciezka.relative_to(baza).as_posix())
    return sorted(przeniesione)


if __name__ == "__main__":
    zrodlo = input()
    cel = input()

    if not Path(zrodlo).is_dir():
        print("Folder nie istnieje.")
    else:
        przeniesione = przenies_pliki_csv(zrodlo, cel)
        if przeniesione:
            print("\n".join(przeniesione))
        else:
            print("Brak plików.")
