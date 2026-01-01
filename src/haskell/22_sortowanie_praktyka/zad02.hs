{-
ZAD-02 — Sortowanie słów w zdaniu

\**Poziom:** ★★☆
\**Tagi:** `sort`, `string`, `split`

### Treść

Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.

### Wejście

\* 1 linia: napis `zdanie`

### Wyjście

\* 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`

### Przykład

\**Wejście:**

```
Lemur wygina śmiało ciało
```

\**Wyjście:**

```
['Lemur', 'ciało', 'wygina', 'śmiało']
```

### Uwagi o formatowaniu

\* Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
\* Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to, co w tekście.

-}

import Data.List (sort)
import Data.Char (isAlpha)

-- Sortowanie słów w zdaniu
-- Złożoność czasowa: O(n log n)
-- Złożoność pamięciowa: O(n)
-- Funkcja pomocnicza do filtrowania tylko liter
filterWord :: String -> String
filterWord = filter isAlpha

-- Funkcja do formatowania listy słów w formacie ['word1', 'word2', ...]
formatList :: [String] -> String
formatList xs = "[" ++ intercalate ", " (map (\x -> "'" ++ x ++ "'") xs) ++ "]"
  where
    intercalate sep = concat . intersperse sep
    intersperse _ [] = []
    intersperse _ [x] = [x]
    intersperse sep (x:xs) = x : sep : intersperse sep xs

main :: IO ()
main = do
    zdanie <- getLine
    let slowa = words zdanie
    let czysteSlowa = filter (not . null) $ map filterWord slowa
    let posortowane = sort czysteSlowa
    putStrLn $ formatList posortowane
