{-
ZAD-05 — Wyodrębnij cyfry z tekstu

\**Poziom:** ★☆☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).

### Wejście

Jedna linia:

\* `tekst`

### Wyjście

Jedna linia:

\* napis złożony tylko z cyfr z tekstu wejściowego

### Przykład

\**Wejście:**

```
Terminator2001
```

\**Wyjście:**

```
2001
```

-}

import Data.Char (isDigit)

-- Wyodrębnij cyfry z tekstu
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
extractDigits :: String -> String
extractDigits = filter isDigit

main :: IO ()
main = do
  text <- getLine
  putStrLn $ extractDigits text
