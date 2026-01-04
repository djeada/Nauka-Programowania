{-
ZAD-04 — Zamień wszystkie małe litery na duże

\**Poziom:** ★☆☆
\**Tagi:** `string`, `upper`

### Treść

Wczytaj napis i zamień wszystkie litery na wielkie.

### Wejście

\* 1. linia: napis

### Wyjście

\* 1. linia: napis po konwersji

### Przykład

\**Wejście:**

```
Rumcajs
```

\**Wyjście:**

```
RUMCAJS
```

-}

import Data.Char (toUpper)

-- Zamienia wszystkie litery na wielkie
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  napis <- getLine
  putStrLn $ map toUpper napis
