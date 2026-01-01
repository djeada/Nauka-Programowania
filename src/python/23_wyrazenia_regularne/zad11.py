"""
ZAD-11 — Nazwa pliku bez rozszerzenia

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Otrzymujesz napis reprezentujący pełną ścieżkę do pliku. Wyodrębnij nazwę pliku (bez katalogów) i usuń rozszerzenie (część po ostatniej kropce). Zwróć samą nazwę bez rozszerzenia.

Ścieżka może zawierać separator `\` lub `/`.

### Wejście

Jedna linia:

* `sciezka`

### Wyjście

Jedna linia:

* `nazwa_pliku_bez_rozszerzenia`

### Przykład

**Wejście:**

```
C:\my-long\path_directory\file.html
```

**Wyjście:**

```
file
```

"""

import re


def nazwa_pliku(sciezka):
    """
    Funkcja zwraca nazwe pliku z podanej sciezki.
    """
    nazwa = re.search(r'[^\\/:*?"<>|]+$', sciezka).group(0)

    # usun rozszerzenie pliku
    while re.sub(r"\.[^.]+$", "", nazwa) is not nazwa:
        nazwa = re.sub(r"\.[^.]+$", "", nazwa)
    return nazwa


def test_nazwa_pliku():
    assert nazwa_pliku("C:\\Windows\\explorer.exe") == "explorer"
    assert nazwa_pliku("/home/user/var/log/syslog") == "syslog"
    assert nazwa_pliku("test.jpg.png.mp3.mp5.html.txt") == "test"
    assert nazwa_pliku("test") == "test"


if __name__ == "__main__":
    test_nazwa_pliku()
