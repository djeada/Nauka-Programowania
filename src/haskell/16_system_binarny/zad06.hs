{-
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

\**Poziom:** ★★☆
\**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

\**Wejście:**

```
4301
10
4
```

\**Wyjście:**

```
1003031
```

### Uwagi o formacie

\* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
\* Dla wartości 10..35 stosuj `A..Z`.

-}

import Data.Char (chr, digitToInt, intToDigit, isHexDigit, ord, toUpper)
import Numeric (readInt, showIntAtBase)

-- Konwertuje liczbę z systemu o podstawie p na dziesiętną
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(1)
fromBase :: Int -> String -> Int
fromBase base = foldl (\acc c -> acc * base + charToDigit c) 0
  where
    charToDigit c
      | c >= '0' && c <= '9' = ord c - ord '0'
      | c >= 'A' && c <= 'Z' = ord c - ord 'A' + 10
      | c >= 'a' && c <= 'z' = ord c - ord 'a' + 10
      | otherwise = 0

-- Konwertuje liczbę dziesiętną na system o podstawie q
-- Złożoność czasowa: O(log_q n)
-- Złożoność pamięciowa: O(log_q n)
toBase :: Int -> Int -> String
toBase _ 0 = "0"
toBase base n = reverse $ go n
  where
    go 0 = ""
    go x = digitToChar (x `mod` base) : go (x `div` base)
    digitToChar d
      | d < 10 = chr (ord '0' + d)
      | otherwise = chr (ord 'A' + d - 10)

-- Konwersja między dowolnymi systemami (2..36)
main :: IO ()
main = do
  x <- getLine
  p <- readLn :: IO Int
  q <- readLn :: IO Int
  let decimal = fromBase p x
  putStrLn $ toBase q decimal
