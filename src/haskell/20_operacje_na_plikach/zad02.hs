{-
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

-}
main :: IO ()
main = pure ()
