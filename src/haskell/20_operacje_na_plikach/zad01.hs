{-
ZAD-01 — Czy ścieżka istnieje?

\**Poziom:** ★☆☆
\**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego **pliku lub folderu**.

### Wejście

\* 1 linia: `path` (napis — ścieżka)

### Wyjście

\* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

\**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

\**Wyjście:**

```
Prawda
```

-}

import System.Directory (doesPathExist)

-- Sprawdza czy ścieżka istnieje
-- Złożoność czasowa: O(1) - operacja systemowa
-- Złożoność pamięciowa: O(1)
main :: IO ()
main = do
  path <- getLine
  exists <- doesPathExist path
  putStrLn $ if exists then "Prawda" else "Fałsz"
