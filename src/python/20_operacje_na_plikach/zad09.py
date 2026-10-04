r"""
ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Wczytaj ścieżkę folderu. Usuń wszystkie pliki większe niż **10 kB**, czyli o rozmiarze **większym niż 10240 bajtów**, z tego folderu **i wszystkich jego podfolderów**. Pliki o rozmiarze dokładnie 10240 bajtów zostają. Foldery zostają, nawet jeśli staną się puste.

Rozmiar to liczba bajtów na dysku, a nie liczba znaków w pliku — w kodowaniu UTF-8 litera `ą` zajmuje 2 bajty.

### Wejście

* 1. linia: ścieżka folderu

### Wyjście

* Ścieżki usuniętych plików względem podanego folderu, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli żaden plik nie został usunięty.
* `Folder nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego folderu.

### Przykład

**Pliki przed:**

```
pobrane/film.mp4 (rozmiar: 50000 B)
pobrane/notatka.txt (rozmiar: 300 B)
pobrane/obrazy/duże.png (rozmiar: 10241 B)
pobrane/obrazy/ikona.png (rozmiar: 10240 B)
```

**Wejście:**

```
pobrane
```

**Wyjście:**

```
film.mp4
obrazy/duże.png
```

**Pliki po:**

```
pobrane/film.mp4 (usunięty)
pobrane/notatka.txt (rozmiar: 300 B)
pobrane/obrazy/duże.png (usunięty)
pobrane/obrazy/ikona.png (rozmiar: 10240 B)
```

`ikona.png` ma dokładnie 10240 bajtów, więc zostaje.

### Uwagi

* Rozmiar pliku w bajtach zwraca `os.path.getsize()` albo `Path.stat().st_size`, a plik usuwa `os.remove()` albo `Path.unlink()`.

"""

from pathlib import Path

LIMIT_BAJTOW = 10240  # 10 kB


def usun_duze_pliki(folder, limit=LIMIT_BAJTOW):
    """Usuwa pliki większe niż limit bajtów; zwraca posortowane ścieżki usuniętych plików."""
    baza = Path(folder)
    usuniete = []
    for sciezka in sorted(baza.rglob("*")):
        if sciezka.is_file() and sciezka.stat().st_size > limit:
            sciezka.unlink()
            usuniete.append(sciezka.relative_to(baza).as_posix())
    return sorted(usuniete)


if __name__ == "__main__":
    folder = input()

    if not Path(folder).is_dir():
        print("Folder nie istnieje.")
    else:
        usuniete = usun_duze_pliki(folder)
        if usuniete:
            print("\n".join(usuniete))
        else:
            print("Brak plików.")
