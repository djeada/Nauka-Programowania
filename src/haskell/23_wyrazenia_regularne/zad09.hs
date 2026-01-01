{-
ZAD-09 — Usuń fragment napisu od pierwszego wystąpienia słowa klucz

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz tekst (wiele zdań lub wierszy) oraz słowo klucz. Jeśli słowo klucz wystąpi w tekście, usuń całą część od **pierwszego wystąpienia** tego słowa do końca tekstu. Jeśli słowo klucz nie występuje, wypisz tekst bez zmian.

### Wejście

Dwie części:

1. Tekst (może mieć wiele wierszy)
2. W osobnej linii: `klucz`

### Wyjście

Zmodyfikowany tekst.

### Przykład

\*(jak w treści zadania — długi tekst)*

-}

import Data.Char (isDigit)

-- Ekstrakcja wszystkich numerów z tekstu
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)
extractNumbers :: String -> [String]
extractNumbers [] = []
extractNumbers text = 
    case dropWhile (not . isDigit) text of
        [] -> []
        rest -> 
            let (num, remaining) = span isDigit rest
            in num : extractNumbers remaining

main :: IO ()
main = do
    text <- getLine
    print $ extractNumbers text
