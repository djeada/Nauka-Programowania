{-
ZAD-05 — k-ta pochodna wielomianu

\**Poziom:** ★★☆
\**Tagi:** `pochodna`, `wielomiany`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

### Wejście

\* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
\* 2. linia: `n+1` liczb: `a_n ... a_0`
\* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

\* Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
\* Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.

### Przykład

\**Wejście:**

```
2
4 -3 2
1
```

\**Wyjście:**

```
8 -3
```

### Uwagi o formatowaniu

\* Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:
  `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]`.

-}

import Data.List (intercalate)

-- Oblicza k-tą pochodną wielomianu
-- Złożoność czasowa: O(n*k), gdzie n to stopień wielomianu
-- Złożoność pamięciowa: O(n)
kthDerivative :: [Int] -> Int -> [Int]
kthDerivative coeffs 0 = coeffs
kthDerivative [] _ = []
kthDerivative coeffs k
    | k < 0 = coeffs
    | k >= length coeffs = []
    | otherwise = kthDerivative (derivative coeffs) (k - 1)
    where
        derivative [] = []
        derivative [_] = []
        derivative cs = zipWith (*) [length cs - 1, length cs - 2 .. 1] (init cs)

-- k-ta pochodna wielomianu (z I/O)
main :: IO ()
main = do
    n <- readLn :: IO Int
    coeffs <- map read . words <$> getLine :: IO [Int]
    k <- readLn :: IO Int
    let result = kthDerivative coeffs k
    if null result
        then putStrLn "[]"
        else putStrLn $ intercalate " " $ map show result
