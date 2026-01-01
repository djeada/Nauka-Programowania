{-
ZAD-07 — Różnica między dwoma listami

\**Poziom:** ★☆☆
\**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz elementy, które występują **tylko w jednej** z list (różnica symetryczna).

\* Kolejność elementów w wyniku może być **dowolna**.
\* Jeśli wszystkie elementy są wspólne — wypisz `[]`.

### Wejście

\* 1 linia: lista 1
\* 2 linia: lista 2

### Wyjście

\* 1 linia: lista elementów niewspólnych

### Przykład

\**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

\**Wyjście (jedna z poprawnych odpowiedzi):**

```
[9, 5, 1]
```

-}
main :: IO ()
main = do
  list1Str <- getLine
  list2Str <- getLine
  
  let parseList str = read str :: [Int]
  let list1 = parseList list1Str
  let list2 = parseList list2Str
  
  let onlyIn1 = [x | x <- list1, x `notElem` list2]
  let onlyIn2 = [x | x <- list2, x `notElem` list1]
  let result = onlyIn1 ++ onlyIn2
  
  print result
