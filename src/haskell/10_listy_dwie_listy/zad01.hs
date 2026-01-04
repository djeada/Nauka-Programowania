{-
ZAD-01 — Wypisanie elementów dwóch list na przemian

\**Poziom:** ★☆☆
\**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe elementy dłuższej listy w tej samej kolejności.

### Wejście

\* 1 linia: lista 1
\* 2 linia: lista 2

### Wyjście

\* 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**

### Przykład

\**Wejście:**

```
[5, 3, 7, 2]
[1, -2, 3]
```

\**Wyjście:**

```
5,1,3,-2,7,3,2
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
      intercalate sep (x : xs) = x ++ sep ++ intercalate sep xs

  let interleave [] ys = ys
      interleave xs [] = xs
      interleave (x : xs) (y : ys) = x : y : interleave xs ys

  putStrLn $ intercalate "," $ map show $ interleave list1 list2
