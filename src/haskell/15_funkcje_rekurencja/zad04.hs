{-
ZAD-04 — Mnożenie wielomianów

\**Poziom:** ★★☆
\**Tagi:** `wielomiany`, `konwolucja`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich iloczynem.

### Wejście

\* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
\* 2. linia: `n+1` liczb: `a_n ... a_0`
\* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
\* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki iloczynu (długość `n+m+1`), oddzielone spacją.

### Przykład

\**Wejście:**

```
3
5 0 10 6
2
1 2 4
```

\**Wyjście:**

```
5 10 30 26 52 24
```

-}

import Data.List (intercalate)

-- Mnoży dwa wielomiany (konwolucja)
-- Złożoność czasowa: O(n*m), gdzie n, m to stopnie wielomianów
-- Złożoność pamięciowa: O(n+m)
multiplyPolynomials :: [Int] -> [Int] -> [Int]
multiplyPolynomials a b = [sum [a !! i * b !! j | i <- [0..length a - 1], 
                                                     j <- [0..length b - 1], 
                                                     i + j == k] 
                            | k <- [0..length a + length b - 2]]

-- Mnożenie wielomianów (z I/O)
main :: IO ()
main = do
    n <- readLn :: IO Int
    coeffsA <- map read . words <$> getLine :: IO [Int]
    m <- readLn :: IO Int
    coeffsB <- map read . words <$> getLine :: IO [Int]
    putStrLn $ intercalate " " $ map show $ multiplyPolynomials coeffsA coeffsB
