{-
ZAD-07 — Pojemność wody między słupkami

\**Poziom:** ★★★
\**Tagi:** `two pointers`, `prefix`, `trapping rain water`

### Treść

Otrzymujesz listę liczb naturalnych — wysokości słupków. Oblicz, ile jednostek wody może się zatrzymać pomiędzy słupkami po deszczu.

### Wejście

\* 1 linia: lista wysokości `H`

### Wyjście

\* 1 linia: jedna liczba naturalna — ilość wody

### Przykład

\**Wejście:**

```
[3, 0, 1, 0, 2]
```

\**Wyjście:**

```
5
```

-}
import Text.Read (readMaybe)

-- Woda między słupkami
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
trapRainWater :: [Int] -> Int
trapRainWater heights =
  let n = length heights
      leftMax = scanl1 max heights
      rightMax = scanr1 max heights
      water = [min (leftMax !! i) (rightMax !! i) - heights !! i | i <- [0 .. n - 1]]
   in sum water

main :: IO ()
main = do
  input <- getLine
  case readMaybe input :: Maybe [Int] of
    Just heights -> print $ trapRainWater heights
    Nothing -> print (0 :: Int)
