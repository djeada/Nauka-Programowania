{-
ZAD-03 — Suma elementów dwóch list

\**Poziom:** ★☆☆
\**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i zwróć listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
Jeśli któraś lista jest krótsza, brakujące elementy traktuj jako `0`.

### Wejście

\* 1 linia: lista 1
\* 2 linia: lista 2

### Wyjście

\* 1 linia: lista sum

### Przykład

\**Wejście:**

```
[3, 1, 2, 5]
[2, 8, 6, 5]
```

\**Wyjście:**

```
[5, 9, 8, 10]
```

-}
main :: IO ()
main = do
  list1Str <- getLine
  list2Str <- getLine
  
  let parseList str = read str :: [Int]
  let list1 = parseList list1Str
  let list2 = parseList list2Str
  
  let intercalate sep [] = ""
      intercalate sep [x] = x
      intercalate sep (x:xs) = x ++ sep ++ intercalate sep xs
  
  let maxLen = max (length list1) (length list2)
  let list1' = list1 ++ replicate (maxLen - length list1) 0
  let list2' = list2 ++ replicate (maxLen - length list2) 0
  let sums = zipWith (+) list1' list2'
  
  putStrLn $ intercalate "," $ map show sums
