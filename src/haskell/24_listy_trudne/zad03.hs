{-
ZAD-03 — Minimalny iloczyn trzech liczb

\**Poziom:** ★★☆
\**Tagi:** `list`, `min`, `math`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech liczb** wybranych z tej listy.

Jeśli lista zawiera mniej niż 3 liczby — wypisz iloczyn wszystkich elementów listy.

### Wejście

\* 1 linia: lista liczb całkowitych `A`

### Wyjście

\* 1 linia: jedna liczba całkowita

### Przykład

\**Wejście:**

```
[3, -1, -3, 2, 9, 4]
```

\**Wyjście:**

```
-108
```

-}
import Text.Read (readMaybe)
import Data.List (sort)

-- Minimalny iloczyn trzech liczb
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
minProductOfThree :: [Int] -> Int
minProductOfThree xs
    | length xs < 3 = product xs
    | otherwise = 
        let sorted = sort xs
            n = length sorted
            -- Możliwe przypadki dla MINIMUM:
            -- 1. Trzy najmniejsze (mogą być ujemne)
            -- 2. Najmniejsza (najbar dziej ujemna) * dwie największe (dodatnie)
            -- 3. Trzy największe (jeśli wszystkie dodatnie, to będzie max nie min)
            option1 = product $ take 3 sorted
            option2 = sorted !! 0 * sorted !! (n-2) * sorted !! (n-1)
            option3 = product $ drop (n-3) sorted
        in minimum [option1, option2, option3]

main :: IO ()
main = do
    input <- getLine
    case readMaybe input :: Maybe [Int] of
        Just xs -> print $ minProductOfThree xs
        Nothing -> print (0 :: Int)
