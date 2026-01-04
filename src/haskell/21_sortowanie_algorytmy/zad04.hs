{-
ZAD-04 — Sortowanie przez scalanie

\**Poziom:** ★★☆
\**Tagi:** `sorting`, `merge-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez scalanie**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Podziel listę na dwie (w miarę) równe części.
3. Rekurencyjnie posortuj obie części.
4. **Scal** dwie posortowane listy w jedną posortowaną.

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

\* Złożoność czasowa: `O(n log n)`.

-}

import Text.Read (readMaybe)

-- Quicksort
-- Złożoność czasowa: O(n log n) średnio, O(n^2) najgorszy przypadek
-- Złożoność pamięciowa: O(n)
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (pivot : xs) = quicksort smaller ++ [pivot] ++ quicksort larger
  where
    smaller = [x | x <- xs, x <= pivot]
    larger = [x | x <- xs, x > pivot]

parseList :: String -> Maybe [Int]
parseList s = readMaybe s

main :: IO ()
main = do
  input <- getLine
  case parseList input of
    Just xs -> print $ quicksort xs
    Nothing -> print ([] :: [Int])
