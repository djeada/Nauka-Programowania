{-
ZAD-04 — Wczytaj i wypisz treść pliku

\**Poziom:** ★☆☆
\**Tagi:** `files`, `read`, `encoding`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.

### Wejście

\* 1 linia: `file_path`

### Wyjście

\* treść pliku (dokładnie taka jak w pliku)

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents\wiadomość.txt
```

\**Wyjście:**

```
Witaj! To jest przykładowa treść pliku tekstowego.
```

-}

import System.IO (readFile)
import Control.Exception (catch, IOException)

-- Wczytuje i wypisuje treść pliku
-- Złożoność czasowa: O(n), gdzie n to rozmiar pliku
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    filePath <- getLine
    contents <- catch (readFile filePath) 
                      (\e -> do
                          let _ = (e :: IOException)
                          return "Błąd odczytu pliku")
    putStrLn contents
