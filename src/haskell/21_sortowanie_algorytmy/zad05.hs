{-
ZAD-05 — Sortowanie szybkie

\**Poziom:** ★★☆
\**Tagi:** `sorting`, `quick-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **Quick Sort**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Wybierz **pivot** (np. pierwszy element).
3. Podziel elementy na trzy grupy:

   * mniejsze od pivota,
   * równe pivotowi,
   * większe od pivota.
4. Rekurencyjnie posortuj część mniejszych i większych.
5. Sklej wynik: `mniejsze + równe + większe`.

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

\* Średnio: `O(n log n)`, w pesymistycznym przypadku: `O(n^2)`.
\* Wybór pivota ma wpływ na wydajność.

-}

import Text.Read (readMaybe)

-- Mergesort
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
mergesort :: (Ord a) => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort xs = merge (mergesort left) (mergesort right)
  where
    (left, right) = splitAt (length xs `div` 2) xs

    merge [] ys = ys
    merge xs [] = xs
    merge (x : xs) (y : ys)
      | x <= y = x : merge xs (y : ys)
      | otherwise = y : merge (x : xs) ys

parseList :: String -> Maybe [Int]
parseList s = readMaybe s

main :: IO ()
main = do
  input <- getLine
  case parseList input of
    Just xs -> print $ mergesort xs
    Nothing -> print ([] :: [Int])
