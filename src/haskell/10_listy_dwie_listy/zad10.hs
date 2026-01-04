{-
ZAD-10 — Mediana dwóch posortowanych list

\**Poziom:** ★★☆
\**Tagi:** `list`, `median`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych:

\* obie są posortowane rosnąco,
\* obie mają tę samą, niezerową długość.

Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po „złączeniu” obu list).

### Wejście

\* 1 linia: lista 1 (posortowana rosnąco)
\* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

\* 1 linia: mediana jako liczba zmiennoprzecinkowa
  (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)

### Przykład

\**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

\**Wyjście:**

```
4.5
```

-}
main :: IO ()
main = do
  list1Str <- getLine
  list2Str <- getLine

  let parseList str = read str :: [Int]
  let list1 = parseList list1Str
  let list2 = parseList list2Str

  let merge [] ys = ys
      merge xs [] = xs
      merge (x : xs) (y : ys)
        | x < y = x : merge xs (y : ys)
        | otherwise = y : merge (x : xs) ys

  let merged = merge list1 list2
  let len = length merged
  let median =
        if even len
          then fromIntegral (merged !! (len `div` 2 - 1) + merged !! (len `div` 2)) / 2
          else fromIntegral (merged !! (len `div` 2))

  print (median :: Double)
