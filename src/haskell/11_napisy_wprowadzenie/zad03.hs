{-
ZAD-03 — Z ilu słów składa się zdanie?

\**Poziom:** ★☆☆
\**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.

### Wejście

\* 1. linia: zdanie

### Wyjście

\* 1. linia: liczba słów

### Przykład

\**Wejście:**

```
gram na pianinie.
```

\**Wyjście:**

```
3
```

### Uwagi o formatowaniu

\* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

-}

import Data.Char (isPunctuation)

-- Usuwa znaki interpunkcyjne z końców słowa
-- Złożoność czasowa: O(n), gdzie n to długość słowa
-- Złożoność pamięciowa: O(n)
stripPunctuation :: String -> String
stripPunctuation = reverse . dropWhile isPunctuation . reverse . dropWhile isPunctuation

-- Liczy słowa w zdaniu (bez znaków interpunkcyjnych)
-- Złożoność czasowa: O(n), gdzie n to długość zdania
-- Złożoność pamięciowa: O(n)
main :: IO ()
main = do
    zdanie <- getLine
    let slowa = filter (not . null) $ map stripPunctuation $ words zdanie
    print $ length slowa
