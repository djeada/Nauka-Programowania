{-
ZAD-11 — Średnia długość słów

\**Poziom:** ★☆☆
\**Tagi:** `string`, `arytmetyka`

### Treść

Wczytaj zdanie i oblicz średnią długość słów. Wynik ma być liczbą całkowitą.

### Wejście

\* 1. linia: zdanie

### Wyjście

\* 1. linia: średnia długość słów (liczba całkowita)

### Przykład

\**Wejście:**

```
Zepsuty rower.
```

\**Wyjście:**

```
6
```

### Uwagi

\* Licz jako: `suma_dlugosci // liczba_slow` (dzielenie całkowite).

-}

import Data.Char (isPunctuation)

-- Usuwa znaki interpunkcyjne z końców słowa
-- Złożoność czasowa: O(n), gdzie n to długość słowa
-- Złożoność pamięciowa: O(n)
stripPunctuation :: String -> String
stripPunctuation = reverse . dropWhile isPunctuation . reverse . dropWhile isPunctuation

-- Oblicza średnią długość słów (dzielenie całkowite)
-- Złożoność czasowa: O(n), gdzie n to długość zdania
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
  zdanie <- getLine
  let slowa = filter (not . null) $ map stripPunctuation $ words zdanie
  let sumaDlugosci = sum $ map length slowa
  let liczbaSlow = length slowa
  print $ sumaDlugosci `div` liczbaSlow
