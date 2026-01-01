{-
ZAD-02 — Usuń podnapis

\**Poziom:** ★★☆
\**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

\* 1 linia: napis `S`
\* 2 linia: napis `T` (do usunięcia)

### Wyjście

\* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

\**Wejście:**

```
Lezy jezy na wiezy
zy
```

\**Wyjście:**

```
Le je na wie
```

-}
import Data.List (isPrefixOf)

-- Usuń podnapis
-- Złożoność czasowa: O(n*m)
-- Złożoność pamięciowa: O(n)
removeAll :: String -> String -> String
removeAll _ [] = []
removeAll pattern text
    | pattern `isPrefixOf` text = removeAll pattern (drop (length pattern) text)
    | otherwise = head text : removeAll pattern (tail text)

main :: IO ()
main = do
    mainStr <- getLine
    subStr <- getLine
    putStrLn $ removeAll subStr mainStr
