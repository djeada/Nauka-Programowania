{-
ZAD-08 — Najbliższa potęga dwójki (>= n)

\**Poziom:** ★☆☆
\**Tagi:** `potęgi 2`, `bitwise`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz najmniejszą potęgę liczby 2, która jest **większa lub równa** `n`.

### Wejście

\* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: najmniejsze `2^k ≥ n`.

### Przykład

\**Wejście:**

```
111
```

\**Wyjście:**

```
128
```

### Uwagi

\* Dla `n = 0` przyjmij wynik `1`.

-}

import Numeric (showHex)

-- Konwersja na system szesnastkowy
-- Złożoność czasowa: O(log n)
-- Złożoność pamięciowa: O(log n)
main :: IO ()
main = do
  n <- readLn :: IO Int
  putStrLn $ map toUpper $ showHex n ""
  where
    toUpper c = if c >= 'a' && c <= 'z' then toEnum (fromEnum c - 32) else c
