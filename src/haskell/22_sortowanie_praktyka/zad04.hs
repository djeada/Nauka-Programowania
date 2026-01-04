{-
ZAD-04 — Sortowanie napisów według długości

\**Poziom:** ★☆☆
\**Tagi:** `sort`, `string`, `list`

### Treść

Otrzymujesz listę napisów. Posortuj ją rosnąco według długości napisów.

### Wejście

\* 1 linia: liczba naturalna `N`
\* następnie `N` linii: napis (bez spacji)

### Wyjście

\* 1 linia: lista napisów posortowana jak w przykładzie

### Przykład

\**Wejście:**

```
4
abcd
ab
a
abc
```

\**Wyjście:**

```
['a', 'ab', 'abc', 'abcd']
```

-}

import Data.List (intercalate, sortBy)
import Data.Ord (comparing)

-- Sortowanie napisów według długości
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)

-- Funkcja do formatowania listy napisów
formatList :: [String] -> String
formatList xs = "[" ++ intercalate ", " (map (\x -> "'" ++ x ++ "'") xs) ++ "]"

main :: IO ()
main = do
  nStr <- getLine
  let n = read nStr :: Int
  napisy <- readLines n
  let posortowane = sortBy (comparing length) napisy
  putStrLn $ formatList posortowane

-- Funkcja pomocnicza do wczytania N napisów
readLines :: Int -> IO [String]
readLines 0 = return []
readLines n = do
  line <- getLine
  rest <- readLines (n - 1)
  return (line : rest)
