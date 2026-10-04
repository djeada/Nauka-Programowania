r"""
ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Wczytaj ścieżkę pliku tekstowego i wypisz jego treść dokładnie tak, jak jest zapisana w pliku (wiersz po wierszu, razem z pustymi wierszami w środku).

### Wejście

* 1. linia: ścieżka pliku

### Wyjście

* Treść pliku. Pusty plik — nic nie wypisuj.
* `Plik nie istnieje.` — jeśli podana ścieżka nie wskazuje istniejącego pliku (np. wskazuje folder albo nic).

### Przykład

**Pliki przed:**

```
wiadomość.txt
| Witaj!
| To jest przykładowa treść pliku tekstowego.
```

**Wejście:**

```
wiadomość.txt
```

**Wyjście:**

```
Witaj!
To jest przykładowa treść pliku tekstowego.
```

### Przykład 2

**Pliki przed:**

```
wiadomość.txt
| Witaj!
```

**Wejście:**

```
list.txt
```

**Wyjście:**

```
Plik nie istnieje.
```

### Uwagi

* Sprawdzarka ignoruje końcowe spacje w wierszach i puste wiersze na samym końcu wyjścia, więc nie musisz się przejmować tym, czy plik kończy się znakiem nowej linii.

"""

import os


def wczytaj_plik(sciezka):
    """Zwraca całą treść pliku tekstowego."""
    with open(sciezka, encoding="utf-8") as plik:
        return plik.read()


if __name__ == "__main__":
    sciezka = input()

    if os.path.isfile(sciezka):
        print(wczytaj_plik(sciezka), end="")
    else:
        print("Plik nie istnieje.")
