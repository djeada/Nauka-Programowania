{-
ZAD-08 — Wypisanie elementów macierzy spiralnie

\**Poziom:** ★★☆
\**Tagi:** `macierze`, `spirala`

### Treść

Wczytaj macierz `n×m` i wypisz jej elementy spiralnie (zgodnie z ruchem wskazówek zegara), startując z lewego górnego rogu.

### Wejście

\* 1. linia: `n m`
\* następnie `n` wierszy po `m` liczb

### Wyjście

\* 1 linia: elementy spiralnie, oddzielone spacjami

### Przykład

\**Wejście:**

```
3 3
1 2 3
4 5 6
7 8 9
```

\**Wyjście:**

```
1 2 3 6 9 8 7 4 5
```

-}

import Data.List (intercalate)

readMatrix :: Int -> Int -> IO [[Int]]
readMatrix n m = sequence [map read . words <$> getLine | _ <- [1 .. n]]

spiralOrder :: [[Int]] -> [Int]
spiralOrder [] = []
spiralOrder m = go 0 0 (length m) (length (head m)) []
  where
    go top left bottom right acc
      | top >= bottom || left >= right = reverse acc
      | otherwise = go (top + 1) (left + 1) (bottom - 1) (right - 1) acc4
      where
        acc1 = foldl (\a j -> m !! top !! j : a) acc [left .. right - 1]
        acc2 = foldl (\a i -> m !! i !! (right - 1) : a) acc1 [top + 1 .. bottom - 1]
        acc3 =
          if top < bottom - 1
            then foldl (\a j -> m !! (bottom - 1) !! j : a) acc2 [right - 2, right - 3 .. left]
            else acc2
        acc4 =
          if left < right - 1
            then foldl (\a i -> m !! i !! left : a) acc3 [bottom - 2, bottom - 3 .. top + 1]
            else acc3

main :: IO ()
main = do
  line <- getLine
  let [n, m] = map read (words line)
  macierz <- readMatrix n m
  let spiral = spiralOrder macierz
  putStrLn $ intercalate " " $ map show spiral
