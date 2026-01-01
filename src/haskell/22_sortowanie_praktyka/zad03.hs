{-
ZAD-03 — Sortowanie listy par względem kryterium

\**Poziom:** ★☆☆
\**Tagi:** `sort`, `tuple`, `list`

### Treść

Otrzymujesz listę par `(napis, liczba)`.

a) Posortuj pary rosnąco po liczbie.
b) Posortuj pary rosnąco po długości napisu.

Wypisz wyniki dla a) i b) w osobnych liniach.

### Wejście

\* 1 linia: liczba naturalna `N`
\* następnie `N` linii: `napis liczba` (napis bez spacji)

### Wyjście

\* 1 linia: lista par posortowana jak w podpunkcie a)
\* 2 linia: lista par posortowana jak w podpunkcie b)

### Przykład

\**Wejście:**

```
3
ab 3
bca 1
c 2
```

\**Wyjście:**

```
[('bca', 1), ('c', 2), ('ab', 3)]
[('c', 2), ('ab', 3), ('bca', 1)]
```

-}

import Data.List (sortBy, intercalate)
import Data.Ord (comparing)

-- Sortowanie listy par względem kryterium
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)

-- Funkcja do formatowania pary jako ('napis', liczba)
formatPair :: (String, Int) -> String
formatPair (s, n) = "('" ++ s ++ "', " ++ show n ++ ")"

-- Funkcja do formatowania listy par
formatList :: [(String, Int)] -> String
formatList xs = "[" ++ intercalate ", " (map formatPair xs) ++ "]"

main :: IO ()
main = do
    nStr <- getLine
    let n = read nStr :: Int
    pairs <- readPairs n
    -- a) Sortowanie po liczbie
    let sortedByNumber = sortBy (comparing snd) pairs
    putStrLn $ formatList sortedByNumber
    -- b) Sortowanie po długości napisu
    let sortedByLength = sortBy (comparing (length . fst)) pairs
    putStrLn $ formatList sortedByLength

-- Funkcja pomocnicza do wczytania N par
readPairs :: Int -> IO [(String, Int)]
readPairs 0 = return []
readPairs n = do
    line <- getLine
    let [str, numStr] = words line
    let num = read numStr :: Int
    rest <- readPairs (n - 1)
    return ((str, num) : rest)
