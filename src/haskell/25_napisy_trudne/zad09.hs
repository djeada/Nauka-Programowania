{-
ZAD-09 — Najdłuższy wspólny podnapis

\**Poziom:** ★★★
\**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły fragment), który występuje w obu napisach.

### Wejście

\* 1 linia: napis `A`
\* 2 linia: napis `B`

### Wyjście

\* 1 linia: najdłuższy wspólny podnapis
  (jeśli jest kilka o tej samej długości — wybierz ten, który występuje **najwcześniej w A**; jeśli nadal remis, najwcześniej w B)

### Przykład

\**Wejście:**

```
ijkabcdl
xxxxabcd
```

\**Wyjście:**

```
abcd
```

-}
import Data.List (inits, tails)

-- Najdłuższy wspólny podnapis
-- Złożoność czasowa: O(n*m*min(n,m))
-- Złożoność pamięciowa: O(1)
longestCommonSubstring :: String -> String -> String
longestCommonSubstring a b =
  let allSubsA = [sub | t <- tails a, sub <- tail (inits t), not (null sub)]
      commonSubs = filter (`elem` allSubsB) allSubsA
      allSubsB = [sub | t <- tails b, sub <- tail (inits t), not (null sub)]
      longest = if null commonSubs then "" else maximumBy (comparing length) commonSubs
   in longest
  where
    comparing f x y = compare (f x) (f y)
    maximumBy cmp (x : xs) = foldl (\a b -> if cmp a b == GT then a else b) x xs
    maximumBy _ [] = error "empty list"

main :: IO ()
main = do
  a <- getLine
  b <- getLine
  putStrLn $ longestCommonSubstring a b
