{-
ZAD-05 — Usuń powtórzenia sąsiadujących znaków

\**Poziom:** ★★★
\**Tagi:** `string`, `compress`, `run-length`

### Treść

Otrzymujesz napis. Usuń powtórzenia znaków występujących **bezpośrednio obok siebie**, pozostawiając jedno wystąpienie z każdej „serii”.

### Wejście

\* 1 linia: napis `S`

### Wyjście

\* 1 linia: napis po redukcji sąsiadów

### Przykład

\**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

\**Wyjście:**

```
ABA
```

-}
removeConsecutiveDuplicates :: String -> String
removeConsecutiveDuplicates [] = []
removeConsecutiveDuplicates [x] = [x]
removeConsecutiveDuplicates (x : y : xs)
  | x == y = removeConsecutiveDuplicates (x : xs)
  | otherwise = x : removeConsecutiveDuplicates (y : xs)

main :: IO ()
main = do
  text <- getLine
  putStrLn $ removeConsecutiveDuplicates text
