r"""
ZAD-11 — Nazwa pliku bez rozszerzenia

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Wczytaj ścieżkę do pliku. Wyodrębnij z niej nazwę pliku (część po ostatnim separatorze `/` lub `\`; ścieżka może mieszać oba separatory) i usuń z niej rozszerzenie.

**Rozszerzenie** to ostatnia kropka w nazwie pliku razem ze wszystkimi znakami po niej — chyba że ta kropka jest pierwszym znakiem nazwy (np. `.bashrc` nie ma rozszerzenia). Kropki w nazwach folderów nie mają znaczenia. Nazwa bez kropki zostaje bez zmian.

### Wejście

* 1. linia: ścieżka (nie kończy się separatorem)

### Wyjście

Jedna linia: nazwa pliku bez rozszerzenia.

### Przykład

**Wejście:**

```
C:\my-long\path_directory\file.html
```

**Wyjście:**

```
file
```

### Przykład 2

**Wejście:**

```
backup/archiwum.tar.gz
```

**Wyjście:**

```
archiwum.tar
```

### Uwagi

* Nazwę pliku dopasuje wzorzec `[^\\/]+$` („znaki inne niż ukośniki aż do końca napisu”).

"""

import re


def nazwa_bez_rozszerzenia(sciezka):
    nazwa = re.search(r"[^\\/]+$", sciezka).group()
    # Ostatnia kropka i wszystko po niej — o ile przed kropką jest jakiś znak.
    return re.sub(r"(?<=.)\.[^.]*$", "", nazwa)


if __name__ == "__main__":
    sciezka = input()
    print(nazwa_bez_rozszerzenia(sciezka))
