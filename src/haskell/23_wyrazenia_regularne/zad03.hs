{-
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

\* `s`

### Wyjście

Jedna linia:

\* `Prawda` — jeśli napis zawiera tylko cyfry
\* `Fałsz` — w przeciwnym razie

### Przykład

\**Wejście:**

```
1234
```

\**Wyjście:**

```
Prawda
```

-}

import Data.Char (isDigit)

-- Sprawdź, czy napis składa się wyłącznie z cyfr
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(1)
isAllDigits :: String -> Bool
isAllDigits [] = False -- Empty string is not all digits
isAllDigits s = all isDigit s

main :: IO ()
main = do
  s <- getLine
  putStrLn $ if isAllDigits s then "Prawda" else "Fałsz"
