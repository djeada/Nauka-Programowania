{-
ZAD-04 — Dodawanie i odejmowanie macierzy

\**Poziom:** ★☆☆
\**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `n×m`.
a) Wypisz ich sumę.
b) Wypisz różnicę: (pierwsza − druga).

### Wejście

\* 1. linia: `n`
\* 2. linia: `m`
\* potem `n` wierszy pierwszej macierzy (po `m` liczb)
\* potem `n` wierszy drugiej macierzy (po `m` liczb)

### Wyjście

Najpierw `n` wierszy sumy, potem `n` wierszy różnicy (bez dodatkowych napisów).

### Przykład

\**Wejście:**

```
2
2
1 2
-2 0
5 -3
1 7
```

\**Wyjście:**

```
6 -1
-1 7
-4 5
-3 -7
```

-}

import Data.List (intercalate)

readMatrix :: Int -> Int -> IO [[Int]]
readMatrix n m = sequence [map read . words <$> getLine | _ <- [1 .. n]]

addMatrices :: [[Int]] -> [[Int]] -> [[Int]]
addMatrices m1 m2 = [[m1 !! i !! j + m2 !! i !! j | j <- [0 .. length (head m1) - 1]] | i <- [0 .. length m1 - 1]]

subtractMatrices :: [[Int]] -> [[Int]] -> [[Int]]
subtractMatrices m1 m2 = [[m1 !! i !! j - m2 !! i !! j | j <- [0 .. length (head m1) - 1]] | i <- [0 .. length m1 - 1]]

printMatrix :: [[Int]] -> IO ()
printMatrix = mapM_ (putStrLn . intercalate " " . map show)

main :: IO ()
main = do
  n <- readLn :: IO Int
  m <- readLn :: IO Int
  m1 <- readMatrix n m
  m2 <- readMatrix n m
  let suma = addMatrices m1 m2
  let roznica = subtractMatrices m1 m2
  printMatrix suma
  printMatrix roznica
