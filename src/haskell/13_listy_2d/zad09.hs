{-
ZAD-09 — Klepsydra o największej sumie

\**Poziom:** ★★☆
\**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):

```
a b c
  d
e f g
```

### Wejście

\* 1. linia: `n m`
\* następnie `n` wierszy po `m` liczb całkowitych

### Wyjście

\* 1 linia: maksymalna suma klepsydry

### Przykład

\**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

\**Wyjście:**

```
75
```

-}

readMatrix :: Int -> Int -> IO [[Int]]
readMatrix n m = sequence [map read . words <$> getLine | _ <- [1..n]]

hourglassSum :: [[Int]] -> Int -> Int -> Int
hourglassSum m i j = sum [m !! i !! j, m !! i !! (j+1), m !! i !! (j+2),
                           m !! (i+1) !! (j+1),
                           m !! (i+2) !! j, m !! (i+2) !! (j+1), m !! (i+2) !! (j+2)]

maxHourglassSum :: [[Int]] -> Int
maxHourglassSum m = maximum [hourglassSum m i j | i <- [0..n-3], j <- [0..m'-3]]
    where
        n = length m
        m' = length (head m)

main :: IO ()
main = do
    line <- getLine
    let [n, m'] = map read (words line)
    macierz <- readMatrix n m'
    print $ maxHourglassSum macierz
