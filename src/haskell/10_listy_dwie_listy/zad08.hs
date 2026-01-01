{-
ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

\**Poziom:** ★★☆
\**Tagi:** `list`, `merge`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w jedną listę:

\* wynik ma być posortowany rosnąco,
\* wynik ma zawierać **unikalne** elementy (bez duplikatów).

### Wejście

\* 1 linia: lista 1 (posortowana rosnąco)
\* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

\* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

\**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

\**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

-}
main :: IO ()
main = do
  list1Str <- getLine
  list2Str <- getLine
  
  let parseList str = read str :: [Int]
  let list1 = parseList list1Str
  let list2 = parseList list2Str
  
  let merge [] ys = ys
      merge xs [] = xs
      merge (x:xs) (y:ys)
        | x < y = x : merge xs (y:ys)
        | x > y = y : merge (x:xs) ys
        | otherwise = x : merge xs ys  -- usuń duplikaty
  
  print $ merge list1 list2
