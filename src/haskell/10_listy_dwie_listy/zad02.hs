{-
ZAD-02 — Połączenie dwóch list

\**Poziom:** ★☆☆
\**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

\**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
\**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4, …) elementami z drugiej listy o tych samych indeksach — o ile taki indeks istnieje w obu listach.

### Wejście

\* 1 linia: lista 1
\* 2 linia: lista 2

### Wyjście

\* 1 linia: wynik dla **a)** jako lista
\* 2 linia: wynik dla **b)** jako lista

### Przykład

\**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

\**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
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

  -- a) Połącz listy
  putStrLn $ intercalate "," $ map show $ list1 ++ list2

  -- b) Podmień elementy o parzystych indeksach
  let replace = zipWith3 (\i x y -> if even i then y else x) [0 ..] list1 (list2 ++ repeat 0)
  let result = take (length list1) replace
  putStrLn $ intercalate "," $ map show result
