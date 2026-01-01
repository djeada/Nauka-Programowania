{-
ZAD-10 — Obróć macierz o 90° w prawo

\**Poziom:** ★★☆
\**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

\* 1. linia: `n`
\* następnie `n` wierszy po `n` liczb

### Wyjście

\* `n` wierszy obróconej macierzy

### Przykład

\**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

\**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

-}

import Data.List (intercalate, transpose)

readMatrix :: Int -> IO [[Int]]
readMatrix n = sequence [map read . words <$> getLine | _ <- [1..n]]

rotate90 :: [[Int]] -> [[Int]]
rotate90 m = map reverse (transpose m)

main :: IO ()
main = do
    n <- readLn :: IO Int
    macierz <- readMatrix n
    let obrocona = rotate90 macierz
    mapM_ (putStrLn . intercalate " " . map show) obrocona
main = pure ()
