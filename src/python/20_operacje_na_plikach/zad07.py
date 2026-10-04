r"""
ZAD-07 — Dodaj wiersz na początku pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `write`, `prepend`

### Treść

Wczytaj ścieżkę pliku tekstowego i wiersz tekstu. Dopisz ten wiersz na **początku** pliku — jako nowy, pierwszy wiersz. Dotychczasowa treść pliku ma pozostać bez zmian pod nowym wierszem. Pusty plik po zmianie zawiera tylko nowy wiersz.

### Wejście

* 1. linia: ścieżka pliku
* 2. linia: wiersz do dodania (może zawierać spacje)

### Wyjście

* Gdy plik istnieje — nic (wynikiem jest zmieniony plik).
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku. Wtedy nie twórz żadnego pliku.

### Przykład

**Pliki przed:**

```
notatki.txt
| kupić mleko
| zadzwonić do babci
```

**Wejście:**

```
notatki.txt
TODO:
```

**Wyjście:** *(brak)*

**Pliki po:**

```
notatki.txt
| TODO:
| kupić mleko
| zadzwonić do babci
```

### Przykład 2

**Pliki przed:** *(brak)*

**Wejście:**

```
notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

**Wyjście:**

```
Plik nie istnieje.
```

**Pliki po:**

```
notatki.txt (usunięty)
```

Pliku nie było, więc program niczego nie tworzy.

### Uwagi

* Do pliku nie da się „dopisać na początku” — wczytaj całą treść, a potem zapisz plik od nowa: najpierw nowy wiersz, potem starą treść.

"""

import os


def dodaj_wiersz_na_poczatku(sciezka, wiersz):
    """Zapisuje plik od nowa: najpierw nowy wiersz, potem dotychczasowa treść."""
    with open(sciezka, encoding="utf-8") as plik:
        tresc = plik.read()
    with open(sciezka, "w", encoding="utf-8") as plik:
        plik.write(wiersz + "\n" + tresc)


if __name__ == "__main__":
    sciezka = input()
    wiersz = input()

    if os.path.isfile(sciezka):
        dodaj_wiersz_na_poczatku(sciezka, wiersz)
    else:
        print("Plik nie istnieje.")
