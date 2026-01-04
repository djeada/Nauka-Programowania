{-
ZAD-06 — Połączenie posortowanych list (unikalne)

\**Poziom:** ★★★
\**Tagi:** `merge`, `heap`, `unique`, `sorted`

### Treść

Otrzymujesz listę zawierającą `M` posortowanych list liczb naturalnych. Połącz je w jedną **posortowaną** listę zawierającą wszystkie elementy **bez powtórzeń**.

### Wejście

\* 1 linia: lista list (każda wewnętrzna lista jest posortowana)

### Wyjście

\* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

\**Wejście:**

```
[[-6, 23, 29, 33], [6, 22, 35, 71], [5, 19, 21, 37], [-12, -7, -3, 28]]
```

\**Wyjście:**

```
[-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71]
```

-}

import Data.List (nub, sort)
import Text.Read (readMaybe)

-- Połącz posortowane listy bez powtórzeń
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
mergeSortedLists :: [[Int]] -> [Int]
mergeSortedLists lists = nub $ sort $ concat lists

main :: IO ()
main = do
  input <- getLine
  case readMaybe input :: Maybe [[Int]] of
    Just lists -> print $ mergeSortedLists lists
    Nothing -> print ([] :: [Int])
