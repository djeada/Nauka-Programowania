{-
ZAD-10 — Skopiuj pliki PNG do innego folderu (bez podfolderów)

\**Poziom:** ★☆☆
\**Tagi:** `files`, `copy`, `png`, `shutil`

### Treść

Otrzymujesz ścieżkę folderu źródłowego i docelowego. Skopiuj wszystkie pliki `.png` znajdujące się **bezpośrednio** w folderze źródłowym do folderu docelowego.

### Wejście

\* 1 linia: `src_folder`
\* 2 linia: `dst_folder`

### Wyjście

Brak.

### Przykład

\**Wejście:**

```
C:\Users\Username\Obrazy
D:\Backup\Obrazy
```

\**Wyjście:**
\*(brak)*

-}

import System.Directory (listDirectory, doesDirectoryExist)

-- Listuje pliki w folderze
-- Złożoność czasowa: O(n), gdzie n to liczba plików
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    folderPath <- getLine
    exists <- doesDirectoryExist folderPath
    if exists
        then do
            files <- listDirectory folderPath
            print files
        else print ([] :: [String])
