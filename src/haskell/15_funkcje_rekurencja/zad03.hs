{-
ZAD-03 — Suma wielomianów

\**Poziom:** ★☆☆
\**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

\* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
\* 2. linia: `n+1` liczb: `a_n ... a_0`
\* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
\* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

\**Wejście:**

```
2
3 5 2
2
2 -8 1
```

\**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

\* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

-}

import Data.List (intercalate)

-- Dodaje dwa wielomiany
-- Złożoność czasowa: O(max(n, m)), gdzie n, m to stopnie wielomianów
-- Złożoność pamięciowa: O(max(n, m))
addPolynomials :: [Int] -> [Int] -> [Int]
addPolynomials a b = zipWith (+) a' b'
    where
        maxLen = max (length a) (length b)
        a' = replicate (maxLen - length a) 0 ++ a
        b' = replicate (maxLen - length b) 0 ++ b

-- Suma wielomianów (z I/O)
main :: IO ()
main = do
    n <- readLn :: IO Int
    coeffsA <- map read . words <$> getLine :: IO [Int]
    m <- readLn :: IO Int
    coeffsB <- map read . words <$> getLine :: IO [Int]
    putStrLn $ intercalate " " $ map show $ addPolynomials coeffsA coeffsB
