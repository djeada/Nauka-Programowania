{-
ZAD-02 — Iloczyn wielomianu przez skalar

\**Poziom:** ★☆☆
\**Tagi:** `wielomiany`, `listy`, `I/O`

### Treść

Wczytaj współczynniki wielomianu oraz liczbę `k`. Wypisz współczynniki wielomianu powstałego przez pomnożenie każdego współczynnika przez `k`.

### Wejście

\* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
\* 2. linia: `n+1` liczb całkowitych: `a_n ... a_0`
\* 3. linia: `k` — liczba całkowita (skalar)

### Wyjście

Jedna linia: `n+1` liczb całkowitych (współczynniki po mnożeniu), oddzielonych spacją.

### Przykład

\**Wejście:**

```
2
4 -3 2
-2
```

\**Wyjście:**

```
-8 6 -4
```

-}

import Data.List (intercalate)

-- Mnoży wielomian przez skalar
-- Złożoność czasowa: O(n), gdzie n to stopień wielomianu
-- Złożoność pamięciowa: O(n)
multiplyByScalar :: [Int] -> Int -> [Int]
multiplyByScalar coeffs k = map (* k) coeffs

-- Iloczyn wielomianu przez skalar (z I/O)
main :: IO ()
main = do
  n <- readLn :: IO Int
  coeffs <- map read . words <$> getLine :: IO [Int]
  k <- readLn :: IO Int
  putStrLn $ intercalate " " $ map show $ multiplyByScalar coeffs k
