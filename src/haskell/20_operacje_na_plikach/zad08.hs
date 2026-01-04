{-
ZAD-08 — Modyfikacja plików spełniających warunek (rekurencyjnie)

\**Poziom:** ★★☆
\**Tagi:** `files`, `recursive`, `txt`, `csv`

### Treść

Otrzymujesz ścieżkę do folderu. Wykonaj:

a) dopisz swoje inicjały na końcu każdego pliku `.txt` w folderze i podfolderach,
b) usuń **środkowy wiersz** z każdego pliku `.csv` w folderze i podfolderach
(jeśli liczba wierszy jest parzysta — usuń **dolny z dwóch środkowych**).

### Wejście

\* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents\Projekt
```

\**Wyjście:**
\*(brak)*

-}

import Control.Exception (IOException, catch)
import System.Directory (copyFile, doesFileExist)

-- Kopiuje plik
-- Złożoność czasowa: O(n), gdzie n to rozmiar pliku
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
  source <- getLine
  dest <- getLine
  exists <- doesFileExist source
  if exists
    then do
      catch
        (copyFile source dest >> putStrLn "Skopiowano plik")
        ( \e -> do
            let _ = (e :: IOException)
            putStrLn "Błąd kopiowania"
        )
    else putStrLn "Plik źródłowy nie istnieje"
