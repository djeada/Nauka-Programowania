{-
ZAD-06 — Scalanie przedziałów

\**Poziom:** ★★☆
\**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

\* 1. linia: `n`
\* następnie `n` linii: `a_i b_i`

### Wyjście

\* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

\**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

\**Wyjście:**

```
10 22
23 88
```

### Uwagi

\* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

-}

import Data.List (sortBy)
import Data.Ord (comparing)

mergeIntervals :: [(Int, Int)] -> [(Int, Int)]
mergeIntervals [] = []
mergeIntervals intervals = reverse $ foldl merge [head sorted] (tail sorted)
    where
        sorted = sortBy (comparing fst) intervals
        merge [] interval = [interval]
        merge ((a, b):rest) (c, d)
            | c <= b = (a, max b d):rest
            | otherwise = (c, d):(a, b):rest

main :: IO ()
main = do
    n <- readLn :: IO Int
    intervals <- sequence [do
        line <- getLine
        let [a, b] = map read (words line)
        return (a, b) | _ <- [1..n]]
    let merged = mergeIntervals intervals
    mapM_ (\(a, b) -> putStrLn $ show a ++ " " ++ show b) merged
