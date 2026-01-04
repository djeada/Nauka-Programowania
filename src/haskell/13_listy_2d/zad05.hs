{-
ZAD-05 — Czy macierz jest magiczna?

\**Poziom:** ★★☆
\**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami naturalnymi. Sprawdź, czy to **kwadrat magiczny**: suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

\* 1. linia: `n`
\* następnie `n` wierszy po `n` liczb

### Wyjście

\* `Prawda` albo `Fałsz`

### Przykład

\**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

\**Wyjście:**

```
Prawda
```

-}

import Data.List (transpose)

readMatrix :: Int -> IO [[Int]]
readMatrix n = sequence [map read . words <$> getLine | _ <- [1 .. n]]

isMagicSquare :: [[Int]] -> Bool
isMagicSquare m = all (== target) sums
  where
    n = length m
    rowSums = map sum m
    colSums = map sum (transpose m)
    diag1 = sum [m !! i !! i | i <- [0 .. n - 1]]
    diag2 = sum [m !! i !! (n - 1 - i) | i <- [0 .. n - 1]]
    sums = rowSums ++ colSums ++ [diag1, diag2]
    target = head rowSums

main :: IO ()
main = do
  n <- readLn :: IO Int
  macierz <- readMatrix n
  if isMagicSquare macierz
    then putStrLn "Prawda"
    else putStrLn "Fałsz"
