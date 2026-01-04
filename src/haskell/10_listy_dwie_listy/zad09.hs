{-
ZAD-09 — Usuń z pierwszej listy część wspólną obu list

\**Poziom:** ★★☆
\**Tagi:** `list`, `filter`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy, które występują również w drugiej liście.

\* Zachowaj kolejność pozostałych elementów z pierwszej listy.
\* Jeśli wszystko zostanie usunięte — wypisz `[]`.

### Wejście

\* 1 linia: lista 1
\* 2 linia: lista 2

### Wyjście

\* 1 linia: lista 1 po usunięciu elementów wspólnych

### Przykład

\**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

\**Wyjście:**

```
[9, 5]
```

-}
main :: IO ()
main = do
  list1Str <- getLine
  list2Str <- getLine

  let parseList str = read str :: [Int]
  let list1 = parseList list1Str
  let list2 = parseList list2Str

  let result = [x | x <- list1, x `notElem` list2]

  print result
