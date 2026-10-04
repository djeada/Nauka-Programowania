r"""
ZAD-08 — Modyfikacja plików spełniających warunek (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `recursive`, `txt`, `csv`

### Treść

Wczytaj ścieżkę folderu i inicjały (np. `A.D.`). W tym folderze **i wszystkich jego podfolderach**:

a) do każdego pliku `.txt` dopisz inicjały jako nowy, **ostatni wiersz**,

b) z każdego pliku `.csv` usuń **środkowy wiersz** — gdy liczba wierszy jest parzysta, usuń **dolny** z dwóch środkowych.

Pozostałych plików nie zmieniaj. Na koniec wypisz ścieżki wszystkich zmienionych plików.

Szczegóły:

* Wiersze liczymy jak w `str.splitlines()`: znak nowej linii na końcu pliku nie tworzy dodatkowego, pustego wiersza.
* Inicjały trafiają bezpośrednio pod dotychczasowy ostatni wiersz, bez pustego wiersza pomiędzy — także wtedy, gdy plik nie kończy się znakiem nowej linii. Pusty plik `.txt` po zmianie zawiera tylko inicjały.
* W pliku `.csv` o $n$ wierszach usuwamy wiersz numer $\lfloor n/2 \rfloor + 1$ (licząc od 1): przy 3 wierszach — 2., przy 4 — 3., przy 1 — jedyny wiersz.

### Wejście

* 1. linia: ścieżka folderu
* 2. linia: inicjały

### Wyjście

* Ścieżki zmienionych plików względem podanego folderu, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli nie ma żadnego pliku `.txt` ani `.csv`.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Ograniczenia

* Każdy plik `.csv` ma co najmniej jeden wiersz.

### Przykład

**Pliki przed:**

```
projekt/opis.txt
| Projekt X
projekt/dane.csv
| a,1
| b,2
| c,3
projekt/main.py
| print("Projekt X")
projekt/2024/raport.txt
| Raport roczny
projekt/2024/wyniki.csv
| x,1
| y,2
| z,3
| w,4
```

**Wejście:**

```
projekt
A.D.
```

**Wyjście:**

```
2024/raport.txt
2024/wyniki.csv
dane.csv
opis.txt
```

**Pliki po:**

```
projekt/opis.txt
| Projekt X
| A.D.
projekt/dane.csv
| a,1
| c,3
projekt/main.py
| print("Projekt X")
projekt/2024/raport.txt
| Raport roczny
| A.D.
projekt/2024/wyniki.csv
| x,1
| y,2
| w,4
```

`dane.csv` ma 3 wiersze, więc traci 2. wiersz; `wyniki.csv` ma 4 wiersze, więc traci 3. wiersz. Plik `main.py` się nie zmienia.

### Uwagi

* Najpierw zbierz listę wszystkich plików (np. `sorted(Path(folder).rglob("*"))`), a dopiero potem je zmieniaj.

"""

from pathlib import Path


def dopisz_inicjaly(sciezka, inicjaly):
    """Dopisuje inicjały jako nowy, ostatni wiersz pliku."""
    tresc = sciezka.read_text(encoding="utf-8")
    if tresc and not tresc.endswith("\n"):
        tresc += "\n"
    sciezka.write_text(tresc + inicjaly + "\n", encoding="utf-8")


def usun_srodkowy_wiersz(sciezka):
    """Usuwa środkowy wiersz (przy parzystej liczbie wierszy — dolny z dwóch środkowych)."""
    wiersze = sciezka.read_text(encoding="utf-8").splitlines()
    del wiersze[len(wiersze) // 2]
    sciezka.write_text("".join(wiersz + "\n" for wiersz in wiersze), encoding="utf-8")


def modyfikuj_pliki(folder, inicjaly):
    """Zmienia pliki .txt i .csv w folderze i podfolderach; zwraca ich posortowane ścieżki."""
    baza = Path(folder)
    zmienione = []
    for sciezka in sorted(baza.rglob("*")):
        if not sciezka.is_file():
            continue
        rozszerzenie = sciezka.suffix.lower()
        if rozszerzenie == ".txt":
            dopisz_inicjaly(sciezka, inicjaly)
        elif rozszerzenie == ".csv":
            usun_srodkowy_wiersz(sciezka)
        else:
            continue
        zmienione.append(sciezka.relative_to(baza).as_posix())
    return sorted(zmienione)


if __name__ == "__main__":
    folder = input()
    inicjaly = input()

    if not Path(folder).is_dir():
        print("Folder nie istnieje.")
    else:
        zmienione = modyfikuj_pliki(folder, inicjaly)
        if zmienione:
            print("\n".join(zmienione))
        else:
            print("Brak plików.")
