{-
ZAD-02 — Przesuń zera na koniec listy

\**Poziom:** ★★☆
\**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

\* 1 linia: lista liczb całkowitych `A`

### Wyjście

\* 1 linia: lista po przekształceniu

### Przykład

\**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

\**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

-}
import Text.Read (readMaybe)

-- Przesuń zera na koniec listy
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
moveZerosToEnd :: [Int] -> [Int]
moveZerosToEnd xs = 
    let nonZeros = filter (/= 0) xs
        zeros = replicate (length xs - length nonZeros) 0
    in nonZeros ++ zeros

main :: IO ()
main = do
    input <- getLine
    case readMaybe input :: Maybe [Int] of
        Just xs -> print $ moveZerosToEnd xs
        Nothing -> print ([] :: [Int])
