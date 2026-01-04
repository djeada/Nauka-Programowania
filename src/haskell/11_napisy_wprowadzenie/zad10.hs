{-
ZAD-10 — Najdłuższe i najkrótsze słowo

\**Poziom:** ★☆☆
\**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

\* 1. linia: zdanie

### Wyjście

\* 1. linia: najdłuższe słowo
\* 2. linia: najkrótsze słowo

### Przykład

\**Wejście:**

```
Kaczka lubi wiosnę.
```

\**Wyjście:**

```
Kaczka
lubi
```

-}

import Data.Char (isPunctuation)
import Data.List (foldl1')

-- Usuwa znaki interpunkcyjne z końców słowa
-- Złożoność czasowa: O(n), gdzie n to długość słowa
-- Złożoność pamięciowa: O(n)
stripPunctuation :: String -> String
stripPunctuation = reverse . dropWhile isPunctuation . reverse . dropWhile isPunctuation

-- Znajduje najdłuższe i najkrótsze słowo (pierwsze w przypadku remisu)
-- Złożoność czasowa: O(n), gdzie n to długość zdania
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  zdanie <- getLine
  let slowa = filter (not . null) $ map stripPunctuation $ words zdanie
  if null slowa
    then do
      putStrLn ""
      putStrLn ""
    else do
      let najdluzsze = foldl1' (\acc w -> if length w > length acc then w else acc) slowa
      let najkrotsze = foldl1' (\acc w -> if length w < length acc then w else acc) slowa
      putStrLn najdluzsze
      putStrLn najkrotsze
