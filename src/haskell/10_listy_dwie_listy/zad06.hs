{-
ZAD-06 — Znalezienie elementów wspólnych dwóch list

\**Poziom:** ★☆☆
\**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych. Wypisz listę elementów, które występują w obu listach:

\* zachowaj **kolejność występowania w pierwszej liście**,
\* jeśli element z pierwszej listy występuje w drugiej liście, dodaj go do wyniku,
\* jeśli nie ma elementów wspólnych — wypisz `[]`.

### Wejście

\* 1 linia: lista 1
\* 2 linia: lista 2

### Wyjście

\* 1 linia: lista elementów wspólnych

### Przykład

\**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

\**Wyjście:**

```
[2, 4]
```

-}
main :: IO ()
main = do
  list1Str <- getLine
  list2Str <- getLine
  
  let parseList str = read str :: [Int]
  let list1 = parseList list1Str
  let list2 = parseList list2Str
  
  let common = [x | x <- list1, x `elem` list2]
  
  print common
