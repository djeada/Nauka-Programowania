{-
ZAD-05 — Anagramy słowa w zdaniu

\**Poziom:** ★★☆
\**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

\* 1. linia: zdanie
\* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).

### Przykład

\**Wejście:**

```
Sroga kara.
arak
```

\**Wyjście:**

```
kara
```

### Uwagi

\* Tak jak wyżej: usuń interpunkcję z brzegów słów.
\* Porównuj np. posortowane litery w `lower()`.

-}

import Data.Char (isPunctuation, toLower)
import Data.List (sort)

stripPunctuation :: String -> String
stripPunctuation = reverse . dropWhile isPunctuation . reverse . dropWhile isPunctuation

isAnagram :: String -> String -> Bool
isAnagram s1 s2 = sort (map toLower s1) == sort (map toLower s2)

main :: IO ()
main = do
    zdanie <- getLine
    klucz <- getLine
    let slowa = map stripPunctuation $ words zdanie
    let anagramy = filter (\w -> not (null w) && isAnagram w klucz) slowa
    mapM_ putStrLn anagramy
