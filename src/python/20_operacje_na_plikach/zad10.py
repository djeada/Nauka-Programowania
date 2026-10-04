r"""
ZAD-10 — Skopiuj pliki PNG do innego folderu (bez podfolderów)

**Poziom:** ★☆☆
**Tagi:** `files`, `copy`, `png`, `shutil`

### Treść

Wczytaj ścieżkę folderu źródłowego i docelowego. Skopiuj do folderu docelowego wszystkie pliki z rozszerzeniem `.png` (bez względu na wielkość liter), które leżą **bezpośrednio** w folderze źródłowym. Pliki w podfolderach pomiń.

* Pliki w folderze źródłowym zostają na miejscu.
* Jeśli folder docelowy nie istnieje, utwórz go (razem z brakującymi folderami nadrzędnymi). Gdy nie ma czego kopiować, nie ma znaczenia, czy go utworzysz.
* Jeśli w folderze docelowym jest już plik o tej samej nazwie, nadpisz go.

### Wejście

* 1. linia: ścieżka folderu źródłowego
* 2. linia: ścieżka folderu docelowego

### Wyjście

* Nazwy skopiowanych plików, każda w osobnej linii, posortowane rosnąco.
* `Brak plików.` — jeśli w folderze źródłowym nie ma żadnego pliku `.png`.
* `Folder nie istnieje.` — jeśli folder źródłowy nie istnieje. Wtedy niczego nie twórz.

### Przykład

**Pliki przed:**

```
obrazy/kot.png
| (obraz kota)
obrazy/pies.PNG
| (obraz psa)
obrazy/opis.txt
| Zdjęcia zwierząt
obrazy/wakacje/morze.png
| (obraz morza)
```

**Wejście:**

```
obrazy
kopia/obrazy
```

**Wyjście:**

```
kot.png
pies.PNG
```

**Pliki po:**

```
kopia/obrazy/kot.png
| (obraz kota)
kopia/obrazy/pies.PNG
| (obraz psa)
kopia/obrazy/opis.txt (usunięty)
kopia/obrazy/morze.png (usunięty)
obrazy/kot.png
| (obraz kota)
obrazy/pies.PNG
| (obraz psa)
```

Program utworzył folder `kopia/obrazy`. Pliku `wakacje/morze.png` nie kopiujemy, bo leży w podfolderze.

### Uwagi

* Kopiowanie: `shutil.copy(zrodlo, cel)`. Folder razem z folderami nadrzędnymi tworzy `os.makedirs(sciezka, exist_ok=True)`.

"""

import os
import shutil


def skopiuj_pliki_png(zrodlo, cel):
    """Kopiuje pliki .png leżące bezpośrednio w folderze zrodlo do folderu cel."""
    os.makedirs(cel, exist_ok=True)
    skopiowane = []
    for nazwa in sorted(os.listdir(zrodlo)):
        sciezka = os.path.join(zrodlo, nazwa)
        if os.path.isfile(sciezka) and os.path.splitext(nazwa)[1].lower() == ".png":
            shutil.copy(sciezka, os.path.join(cel, nazwa))
            skopiowane.append(nazwa)
    return skopiowane


if __name__ == "__main__":
    zrodlo = input()
    cel = input()

    if not os.path.isdir(zrodlo):
        print("Folder nie istnieje.")
    else:
        skopiowane = skopiuj_pliki_png(zrodlo, cel)
        if skopiowane:
            print("\n".join(skopiowane))
        else:
            print("Brak plików.")
