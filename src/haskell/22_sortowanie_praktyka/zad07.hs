{-
ZAD-07 — Sortowanie listy 0/1/2

\**Poziom:** ★★☆
\**Tagi:** `sort`, `counting`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0`, `1` lub `2`. Posortuj ją rosnąco.

### Wejście

\* 1 linia: liczba naturalna `N`
\* 2 linia: `N` liczb (0/1/2) oddzielonych spacjami

### Wyjście

\* 1 linia: posortowana lista w formacie jak w przykładzie

### Przykład

\**Wejście:**

```
7
1 0 1 2 2 0 1
```

\**Wyjście:**

```
[0, 0, 1, 1, 1, 2, 2]
```

-}

import Data.List (sort, intercalate)

-- Sortowanie listy 0/1/2
-- Złożoność czasowa: O(n log n) lub O(n) przy counting sort
-- Złożoność pamięciowa: O(n)

-- Funkcja do formatowania listy liczb
formatList :: [Int] -> String
formatList xs = "[" ++ intercalate ", " (map show xs) ++ "]"

main :: IO ()
main = do
    nStr <- getLine
    let n = read nStr :: Int
    numsLine <- getLine
    let nums = map read (words numsLine) :: [Int]
    let sorted = sort nums
    putStrLn $ formatList sorted
