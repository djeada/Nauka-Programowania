{-
ZAD-07 — Dodaj wiersz na początku pliku

\**Poziom:** ★☆☆
\**Tagi:** `files`, `write`, `prepend`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego i wiersz tekstu. Dodaj ten wiersz na **początku** pliku.

### Wejście

\* 1 linia: `file_path`
\* 2 linia: `line_to_add` (może zawierać spacje)

### Wyjście

Brak.

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents\notatki.txt
To jest nowy wiersz dodany na początku pliku.
```

\**Wyjście:**
\*(brak)*

-}

import System.IO (appendFile)

-- Dopisuje tekst do pliku
-- Złożoność czasowa: O(n), gdzie n to długość tekstu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    filePath <- getLine
    content <- getLine
    appendFile filePath content
    putStrLn "Dopisano do pliku"
