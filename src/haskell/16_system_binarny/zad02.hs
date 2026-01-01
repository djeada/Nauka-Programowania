{-
ZAD-02A — Wypisz binarnie tylko gdy liczba parzysta

\**Poziom:** ★☆☆
\**Tagi:** `warunki`, `parzystość`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest parzysta — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

\* 1. linia: `n` (liczba naturalna)

### Wyjście

\* Jeśli `n % 2 == 0`: jedna linia z zapisem binarnym `n`
\* W przeciwnym razie: brak wyjścia

### Przykład

\**Wejście:**

```
7
```

\**Wyjście:** *(brak)*

ZAD-02B — Wypisz binarnie tylko gdy liczba pierwsza

\**Poziom:** ★☆☆
\**Tagi:** `pierwszość`, `warunki`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest liczbą pierwszą — wypisz jej zapis binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

\* 1. linia: `n` (liczba naturalna)

### Wyjście

\* Jeśli `n` jest pierwsza: jedna linia z zapisem binarnym `n`
\* W przeciwnym razie: brak wyjścia

### Przykład

\**Wejście:**

```
7
```

\**Wyjście:**

```
111
```

-}

import Numeric (showIntAtBase)
import Data.Char (intToDigit)
import Data.Bits (testBit)

-- Sprawdza czy liczba jest pierwsza
-- Złożoność czasowa: O(sqrt(n))
isPrime :: Int -> Bool
isPrime n
    | n < 2 = False
    | n == 2 = True
    | even n = False
    | otherwise = not $ any (\x -> n `mod` x == 0) [3, 5 .. floor (sqrt (fromIntegral n))]

-- Konwertuje liczbę dziesiętną na binarną
decimalToBinary :: Int -> String
decimalToBinary 0 = "0"
decimalToBinary n = showIntAtBase 2 intToDigit n ""

-- ZAD-02A: Wypisz binarnie tylko gdy parzysta
-- ZAD-02B: Wypisz binarnie tylko gdy pierwsza
main :: IO ()
main = do
    n <- readLn :: IO Int
    -- Sprawdź czy pierwsza (zad02B)
    if isPrime n
        then putStrLn $ decimalToBinary n
        else return ()  -- brak wyjścia dla nieparzystych/nienpierwszych
