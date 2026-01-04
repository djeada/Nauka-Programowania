{-
ZAD-01A — Dziesiętny → binarny

\**Poziom:** ★☆☆
\**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną w systemie dziesiętnym i wypisz jej reprezentację binarną.

### Wejście

\* 1. linia: `n` (liczba naturalna)

### Wyjście

Jedna linia: zapis binarny `n`.

### Przykład

\**Wejście:**

```
3
```

\**Wyjście:**

```
11
```

### Uwagi o formacie

\* Dla `n = 0` wypisz `0`.

ZAD-01B — Binarny → dziesiętny

\**Poziom:** ★☆☆
\**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną w systemie binarnym (ciąg `0/1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

\* 1. linia: `b` (ciąg znaków `0` i `1`)

### Wyjście

Jedna linia: liczba w systemie dziesiętnym.

### Przykład

\**Wejście:**

```
101
```

\**Wyjście:**

```
5
```

-}

import Data.Char (digitToInt, intToDigit, isDigit, isHexDigit, toUpper)
import Numeric (readInt, showIntAtBase)

-- Konwertuje liczbę dziesiętną na binarną
-- Złożoność czasowa: O(log n)
-- Złożoność pamięciowa: O(log n)
decimalToBinary :: Int -> String
decimalToBinary 0 = "0"
decimalToBinary n = showIntAtBase 2 intToDigit n ""

-- Konwertuje liczbę binarną na dziesiętną
-- Złożoność czasowa: O(n), gdzie n to długość napisu
-- Złożoność pamięciowa: O(1)
binaryToDecimal :: String -> Int
binaryToDecimal = foldl (\acc c -> acc * 2 + digitToInt c) 0

-- ZAD-01A: Dziesiętny → binarny
-- ZAD-01B: Binarny → dziesiętny
main :: IO ()
main = do
  input <- getLine
  -- Próbujemy określić czy wejście to liczba binarna czy dziesiętna
  if all (`elem` "01") input && not (null input)
    then print $ binaryToDecimal input -- Binarne → Dziesiętne
    else putStrLn $ decimalToBinary (read input :: Int) -- Dziesiętne → Binarne
