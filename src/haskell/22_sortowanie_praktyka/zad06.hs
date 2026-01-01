{-
ZAD-06 — Sortowanie listy binarnej (0/1)

\**Poziom:** ★★☆
\**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Posortuj ją rosnąco.

### Wejście

\* 1 linia: liczba naturalna `N`
\* 2 linia: `N` liczb (0/1) oddzielonych spacjami

### Wyjście

\* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

\**Wejście:**

```
6
1 0 1 0 1 1
```

\**Wyjście:**

```
[0, 0, 1, 1, 1, 1]
```

-}

import Data.List (sortBy)
import Text.Read (readMaybe)

-- Sortowanie stabilne (Haskell's sort jest stabilny)
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    input <- getLine
    case readMaybe input :: Maybe [Int] of
        Just xs -> print $ sortBy compare xs
        Nothing -> print ([] :: [Int])
