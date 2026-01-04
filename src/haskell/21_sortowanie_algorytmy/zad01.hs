{-
ZAD-01 — Sortowanie bąbelkowe

\**Poziom:** ★☆☆
\**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania bąbelkowego**.
Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów i zamianie ich miejscami, jeśli są w złej kolejności. Powtarzaj przebiegi, aż w całym przebiegu nie zajdzie żadna zamiana.

### Wejście

\* 1 linia: lista liczb całkowitych, np. `[6, 2, 1, 4, 27]`

### Wyjście

\* 1 linia: posortowana lista rosnąco

### Przykład

\**Wejście:**

```
[6, 2, 1, 4, 27]
```

\**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

\* Po każdym pełnym przebiegu największy element „wypływa” na koniec.
\* W kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1.

-}

import Text.Read (readMaybe)

-- Sortowanie bąbelkowe
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(n)
bubbleSort :: (Ord a) => [a] -> [a]
bubbleSort [] = []
bubbleSort xs = bubbleSort' xs (length xs)
  where
    bubbleSort' ys 0 = ys
    bubbleSort' ys n = bubbleSort' (bubble ys) (n - 1)

    bubble [] = []
    bubble [x] = [x]
    bubble (x : y : rest)
      | x > y = y : bubble (x : rest)
      | otherwise = x : bubble (y : rest)

-- Parse listy Haskell-style
parseList :: String -> Maybe [Int]
parseList s = readMaybe s

main :: IO ()
main = do
  input <- getLine
  case parseList input of
    Just xs -> print $ bubbleSort xs
    Nothing -> print ([] :: [Int])
