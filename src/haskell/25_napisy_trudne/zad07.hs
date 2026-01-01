{-
ZAD-07 — Powtarzające się podnapisy

\**Poziom:** ★★★
\**Tagi:** `string`, `substrings`, `count`

### Treść

Otrzymujesz napis. Znajdź wszystkie **podnapisy**, które występują w nim **więcej niż jeden raz**.

### Wejście

\* 1 linia: napis `S`

### Wyjście

\* 1 linia: lista napisów — wszystkie powtarzające się podnapisy

### Przykład

\**Wejście:**

```
pythonpython
```

\**Wyjście:**

```
['python']
```

### Uwagi

\* Jeśli sprawdzarka wymaga konkretnej kolejności (np. rosnąco po długości/alfabetycznie) — musi to być opisane. W przeciwnym razie dopuszczalna może być dowolna kolejność.

-}
import Data.List (tails, inits, nub, sort)

-- Powtarzające się podnapisy
-- Złożoność czasowa: O(n^3)
-- Złożoność pamięciowa: O(n^2)
repeatingSubstrings :: String -> [String]
repeatingSubstrings s = 
    let allSubstrings = [sub | t <- tails s, sub <- tail (inits t), not (null sub)]
        countOccurrences sub = length $ filter (== sub) allSubstrings
        repeated = nub $ filter (\sub -> countOccurrences sub > 1) allSubstrings
    in sort repeated

-- Format as list
formatList :: [String] -> String
formatList xs = "[" ++ concatMap (\x -> "'" ++ x ++ "', ") xs ++ "]"
    where
        concatMap f = concat . map f

main :: IO ()
main = do
    text <- getLine
    let result = repeatingSubstrings text
    -- Format as ['a', 'b'] style
    putStrLn $ "[" ++ unwords (map (\x -> "'" ++ x ++ "'") result) ++ "]"
        where unwords [] = ""
              unwords [x] = x
              unwords (x:xs) = x ++ ", " ++ unwords xs
