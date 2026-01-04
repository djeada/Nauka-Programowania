{-
ZAD-02 — Sortowanie przez wybieranie

\**Poziom:** ★★☆
\**Tagi:** `sorting`, `selection-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wybieranie**.
Dla każdej pozycji `i` znajdź najmniejszy element w zakresie `i..koniec` i zamień go z elementem na pozycji `i`.

### Wejście

\* 1 linia: lista liczb całkowitych

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

\* Złożoność czasowa: `O(n^2)`.

-}

import Data.List (minimumBy)
import Data.Ord (comparing)
import Text.Read (readMaybe)

-- Sortowanie przez wybieranie
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(n)
selectionSort :: (Ord a) => [a] -> [a]
selectionSort [] = []
selectionSort xs = minElem : selectionSort (remove minElem xs)
  where
    minElem = minimum xs
    remove _ [] = []
    remove y (z : zs)
      | y == z = zs
      | otherwise = z : remove y zs

parseList :: String -> Maybe [Int]
parseList s = readMaybe s

main :: IO ()
main = do
  input <- getLine
  case parseList input of
    Just xs -> print $ selectionSort xs
    Nothing -> print ([] :: [Int])
