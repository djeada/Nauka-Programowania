{-
ZAD-08 — Najdłuższy wspólny przedrostek

\**Poziom:** ★★★
\**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.

### Wejście

\* 1 linia: `n` — liczba napisów
\* kolejne `n` linii: napisy

### Wyjście

\* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

\**Wejście:**

```
3
Remolada
Remux
Remmy
```

\**Wyjście:**

```
Rem
```

-}
-- Najdłuższy wspólny przedrostek
-- Złożoność czasowa: O(n*m) gdzie n to liczba napisów, m to długość najkrótszego
-- Złożoność pamięciowa: O(m)
longestCommonPrefix :: [String] -> String
longestCommonPrefix [] = ""
longestCommonPrefix strs = 
    let minLen = minimum $ map length strs
        findPrefix len
            | len == 0 = ""
            | all (\s -> take len (head strs) == take len s) strs = take len (head strs)
            | otherwise = findPrefix (len - 1)
    in findPrefix minLen

main :: IO ()
main = do
    n <- readLn :: IO Int
    strs <- sequence $ replicate n getLine
    putStrLn $ longestCommonPrefix strs
