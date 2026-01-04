{-
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

\**Poziom:** ★★☆
\**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

\* 1 linia: `folder_path`
\* 2 linia: `ext` (np. `.txt`)

### Wyjście

\* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents
.txt
```

\**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

\* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje do `.txt`).

-}

import Data.List (isSuffixOf)
import System.Directory (doesDirectoryExist, listDirectory)
import System.FilePath (takeExtension)

-- Znajduje pliki o danym rozszerzeniu w folderze
-- Złożoność czasowa: O(n), gdzie n to liczba plików
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  folderPath <- getLine
  ext <- getLine
  exists <- doesDirectoryExist folderPath
  if exists
    then do
      files <- listDirectory folderPath
      let matching = filter (isSuffixOf ext) files
      print matching
    else print ([] :: [String])
