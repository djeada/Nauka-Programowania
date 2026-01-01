{-
ZAD-07 — Zamiana sąsiadujących bitów

\**Poziom:** ★☆☆
\**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:

\* bit 0 z bitem 1,
\* bit 2 z bitem 3,
\* bit 4 z bitem 5,
\* itd.

Następnie wypisz wynik w systemie dziesiętnym.

### Wejście

\* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Przykład

\**Wejście:**

```
9131
```

\**Wyjście:**

```
4951
```

### Uwagi

\* Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

-}

import Numeric (showIntAtBase, showOct)
import Data.Char (intToDigit)

-- Konwersja na system ósemkowy
-- Złożoność czasowa: O(log n)
-- Złożoność pamięciowa: O(log n)
main :: IO ()
main = do
    n <- readLn :: IO Int
    putStrLn $ showOct n ""
