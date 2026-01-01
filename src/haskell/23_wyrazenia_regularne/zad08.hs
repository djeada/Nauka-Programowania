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

import Data.Char (isDigit)

-- Walidacja kodu pocztowego (format: XX-XXX gdzie X to cyfra)
-- Złożoność czasowa: O(1)
-- Złożoność pamięciowa: O(1)
validatePostalCode :: String -> Bool
validatePostalCode code = 
    length code == 6 &&
    all isDigit (take 2 code) &&
    code !! 2 == '-' &&
    all isDigit (drop 3 code)

main :: IO ()
main = do
    code <- getLine
    putStrLn $ if validatePostalCode code then "Prawda" else "Fałsz"
