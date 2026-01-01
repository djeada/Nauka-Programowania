{-
ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

\**Poziom:** ★★☆
\**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Otrzymujesz ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze **> 10240 bajtów** w tym folderze i jego podfolderach.

### Wejście

\* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents\DoUsunięcia
```

\**Wyjście:**
\*(brak)*

-}

import System.Directory (removeFile, doesFileExist)
import Control.Exception (catch, IOException)

-- Usuwa plik
-- Złożoność czasowa: O(1)
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
    filePath <- getLine
    exists <- doesFileExist filePath
    if exists
        then do
            catch (removeFile filePath >> putStrLn "Usunięto plik")
                  (\e -> do
                      let _ = (e :: IOException)
                      putStrLn "Błąd usuwania")
        else putStrLn "Plik nie istnieje"
