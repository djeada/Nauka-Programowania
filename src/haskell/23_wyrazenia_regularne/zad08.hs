{-
ZAD-08 — Cyfry w słowach

\**Poziom:** ★★☆
\**Tagi:** `regex`, `string`

### Treść

Otrzymujesz zdanie. Wyodrębnij wszystkie ciągi cyfr, które są częścią słów (czyli są bezpośrednio połączone z literami). Nie uwzględniaj cyfr oddzielonych od liter spacjami.

### Wejście

Jedna linia:

\* `zdanie`

### Wyjście

Każdy znaleziony ciąg cyfr w osobnej linii (w kolejności występowania).

### Przykład

\**Wejście:**

```
Jerzy29 i An37a s3łuchali91 lekcji 22 z języka polskiego
```

\**Wyjście:**

```
29
37
3
91
```

-}

import Data.Char (isDigit, isAlpha)

-- Cyfry w słowach (cyfry połączone z literami)
-- Złożoność czasowa: O(n)
-- Złożoność pamięciowa: O(n)

-- Sprawdź czy słowo zawiera zarówno literę jak i cyfrę
hasLetterAndDigit :: String -> Bool
hasLetterAndDigit w = any isAlpha w && any isDigit w

-- Wyodrębnij ciągi cyfr z słowa
extractDigitsFromWord :: String -> [String]
extractDigitsFromWord [] = []
extractDigitsFromWord text = 
    case dropWhile (not . isDigit) text of
        [] -> []
        rest -> 
            let (num, remaining) = span isDigit rest
            in num : extractDigitsFromWord remaining

main :: IO ()
main = do
    sentence <- getLine
    let wordsWithDigits = filter hasLetterAndDigit (words sentence)
        allDigits = concatMap extractDigitsFromWord wordsWithDigits
    mapM_ putStrLn allDigits
