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

import Data.List (sortBy)
import Data.Ord (comparing)
import Text.Read (readMaybe)

-- Sortowanie po drugim elemencie krotki
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    input <- getLine
    case readMaybe input :: Maybe [(Int, Int)] of
        Just pairs -> do
            let sorted = sortBy (comparing snd) pairs
            print sorted
        Nothing -> print ([] :: [(Int, Int)])
