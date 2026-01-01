{-
ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

\**Poziom:** ★★★
\**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`. Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk.

### Wejście

\* 1 linia: lista `prices` (długości 1..n)
\* 2 linia: `n` (liczba naturalna)

### Wyjście

\* 1 linia: maksymalny zysk (liczba całkowita)

### Przykład

\**Wejście:**

```
[1, 5, 8, 9, 10, 17, 17, 20]
4
```

\**Wyjście:**

```
10
```

-}
import Text.Read (readMaybe)

-- Cięcie sznurka (maksymalny zysk)
-- Złożoność czasowa: O(n^2)
-- Złożoność pamięciowa: O(n)
maxProfit :: [Int] -> Int -> Int
maxProfit prices n
    | n == 0 = 0
    | n < 0 = 0
    | otherwise = maximum [prices !! (i-1) + maxProfit prices (n - i) | i <- [1..min n (length prices)]]

main :: IO ()
main = do
    pricesInput <- getLine
    nInput <- getLine
    case (readMaybe pricesInput :: Maybe [Int], readMaybe nInput :: Maybe Int) of
        (Just prices, Just n) -> print $ maxProfit prices n
        _ -> print (0 :: Int)
