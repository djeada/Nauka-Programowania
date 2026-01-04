{-
ZAD-07 — Zerowanie macierzy

\**Poziom:** ★★☆
\**Tagi:** `macierze`, `indeksy`

### Treść

Wczytaj macierz `n×m`. Jeśli w macierzy występuje `0`, to **cały wiersz i cała kolumna** tego zera mają zostać ustawione na `0` (dla wszystkich zer naraz).

### Wejście

\* 1. linia: `n m`
\* następnie `n` wierszy po `m` liczb

### Wyjście

\* `n` wierszy zmodyfikowanej macierzy

### Przykład

\**Wejście:**

```
3 3
1 2 3
4 0 6
7 8 9
```

\**Wyjście:**

```
1 0 3
0 0 0
7 0 9
```

-}

import Data.List (intercalate)
import qualified Data.Set as Set

readMatrix :: Int -> Int -> IO [[Int]]
readMatrix n m = sequence [map read . words <$> getLine | _ <- [1 .. n]]

findZeros :: [[Int]] -> [(Int, Int)]
findZeros m = [(i, j) | i <- [0 .. length m - 1], j <- [0 .. length (head m) - 1], m !! i !! j == 0]

zeroMatrix :: [[Int]] -> [[Int]]
zeroMatrix m =
  [ [ if i `Set.member` zeroRows || j `Set.member` zeroCols then 0 else m !! i !! j
      | j <- [0 .. length (head m) - 1]
    ]
    | i <- [0 .. length m - 1]
  ]
  where
    zeros = findZeros m
    zeroRows = Set.fromList [i | (i, _) <- zeros]
    zeroCols = Set.fromList [j | (_, j) <- zeros]

main :: IO ()
main = do
  line <- getLine
  let [n, m] = map read (words line)
  macierz <- readMatrix n m
  let zeroed = zeroMatrix macierz
  mapM_ (putStrLn . intercalate " " . map show) zeroed
