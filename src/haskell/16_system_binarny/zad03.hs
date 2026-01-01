{-
ZAD-03A — Dodawanie bitowe

\**Poziom:** ★☆☆
\**Tagi:** `bitwise`, `XOR`, `AND`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Oblicz `a + b` używając wyłącznie operatorów bitowych (i przesunięć).

### Wejście

\* 1. linia: `a`
\* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a + b`.

### Przykład

\**Wejście:**

```
2
3
```

\**Wyjście:**

```
5
```

ZAD-03B — Odejmowanie bitowe

\**Poziom:** ★☆☆
\**Tagi:** `bitwise`, `pożyczki`, `XOR`

### Treść

Wczytaj `a` i `b`. Oblicz `a - b` używając wyłącznie operatorów bitowych.

### Wejście

\* 1. linia: `a`
\* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a - b`.

### Ograniczenia / gwarancje

\* Zakładamy, że `a ≥ b` (wynik jest naturalny).

### Przykład

\**Wejście:**

```
7
5
```

\**Wyjście:**

```
2
```

ZAD-03C — Mnożenie bitowe

\**Poziom:** ★☆☆
\**Tagi:** `bitwise`, `shift`, `pętle`

### Treść

Wczytaj `a` i `b`. Oblicz `a * b` używając wyłącznie operatorów bitowych (np. metoda „shift-and-add”).

### Wejście

\* 1. linia: `a`
\* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `a * b`.

### Przykład

\**Wejście:**

```
4
4
```

\**Wyjście:**

```
16
```

ZAD-03D — Dzielenie całkowite bitowe

\**Poziom:** ★☆☆
\**Tagi:** `bitwise`, `dzielenie`, `shift`

### Treść

Wczytaj `a` i `b`. Oblicz `a // b` używając wyłącznie operatorów bitowych.

### Wejście

\* 1. linia: `a`
\* 2. linia: `b`

### Ograniczenia / gwarancje

\* `b > 0`

### Wyjście

Jedna liczba naturalna: `a // b`.

### Przykład

\**Wejście:**

```
9
3
```

\**Wyjście:**

```
3
```

-}

import Data.Bits (xor, (.&.), shiftL, shiftR)

-- Dodawanie bitowe
-- Złożoność czasowa: O(log(max(a,b)))
-- Złożoność pamięciowa: O(1)
bitwiseAdd :: Int -> Int -> Int
bitwiseAdd a 0 = a
bitwiseAdd a b = bitwiseAdd (a `xor` b) ((a .&. b) `shiftL` 1)

-- Odejmowanie bitowe
-- Złożoność czasowa: O(log(max(a,b)))
bitwiseSubtract :: Int -> Int -> Int
bitwiseSubtract a b = bitwiseAdd a (bitwiseAdd (complement b) 1)
    where complement x = xor x (2^32 - 1)  -- dla 32-bitowych liczb

-- Mnożenie bitowe
-- Złożoność czasowa: O(log b)
bitwiseMultiply :: Int -> Int -> Int
bitwiseMultiply a 0 = 0
bitwiseMultiply a b
    | b .&. 1 == 1 = bitwiseAdd a (bitwiseMultiply (a `shiftL` 1) (b `shiftR` 1))
    | otherwise = bitwiseMultiply (a `shiftL` 1) (b `shiftR` 1)

-- Dzielenie bitowe
-- Złożoność czasowa: O(log a)
bitwiseDivide :: Int -> Int -> Int
bitwiseDivide a b = go a b 0
    where
        go dividend divisor quotient
            | dividend < divisor = quotient
            | otherwise = 
                let shift = findShift dividend divisor 0
                    newQuotient = quotient + (1 `shiftL` shift)
                    newDividend = dividend - (divisor `shiftL` shift)
                in go newDividend divisor newQuotient
        findShift dividend divisor shift
            | (divisor `shiftL` (shift + 1)) > dividend = shift
            | otherwise = findShift dividend divisor (shift + 1)

-- Obsługa różnych operacji
main :: IO ()
main = do
    a <- readLn :: IO Int
    b <- readLn :: IO Int
    -- Domyślnie wykonujemy dodawanie (zad03A)
    print $ bitwiseAdd a b
